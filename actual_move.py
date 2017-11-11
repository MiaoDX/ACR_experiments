"""
This is for ACR with hardware, we eval accuracy on the movements of the platform
"""

import os
import json_tricks
import numpy as np

def from_experiment_get_actual_moves(DIR='', tar_move=-np.array([40, 0, 15, 0, 10, 0]),save_json_file='result.json'):

    actual_moves = []


    for i in range(1, 50):
        json_file = os.path.join(DIR, str(i) + '.json')
        if not os.path.isfile(json_file):
            print("All done")
            break

        print(json_file)

        with open(json_file, 'r') as f:
            info = json_tricks.load(f)

        print(info)

        actual_move = np.array(info['acutal_move'])  # type: np.ndarray

        actual_moves.append(actual_move)


    print("actual_moves:{}".format(actual_moves))

    accumulate_move = np.zeros(6)
    for move in actual_moves:
        accumulate_move += move

    print('accumulation move:{}'.format(accumulate_move))


    # with open(save_json_file, 'w') as f:
    #     # import json
    #     # json.dump(traj, f, indent=4, sort_keys=True)
    #     # json.dump(traj, f, indent=4)
    #     json_tricks.dump(traj, f, indent=4, sort_keys=True, primitives=True)


def three_dof_two_errors(json_file='result.json'):
    # Two errors, rotation and translation with precious 3D (x, z and yaw)

    from eval import error_position

    with open(json_file, 'r') as f:
        info = json_tricks.load(f)

    ref_pose = np.array(info['im_ref_pose_6D'])  # type: np.ndarray
    start_pose = np.array(info['poses_6D'])[0]  # type: np.ndarray

    target_movement = ref_pose - start_pose

    print("ref_pose:{}\n start_pose:{}\n target_movement:{}".format(ref_pose, start_pose, target_movement))

    acutal_moves = np.array(info['acutal_moves'])

    errors_yaw = []
    errors_xz = []

    acutal_moves = np.insert(acutal_moves, 0, np.zeros(6), axis=0)  # for calc the init error

    now_movement = np.zeros(6)
    for move in acutal_moves:
        # move[:3] = -move[:3]  # note the minus, for translation
        now_movement += move

        errors_yaw.append(error_position(target_movement[4], now_movement[4]))
        errors_xz.append(error_position([target_movement[0], target_movement[2]], [now_movement[0], now_movement[2]]))

    errors_yaw = np.array(errors_yaw)
    errors_xz = np.array(errors_xz)

    print("errors_yaw:{}\nerrors_xz:{}".format(errors_yaw.T, errors_xz.T))

    print('All num:{}, len(errors):{}'.format(info['num'], len((errors_yaw))))
    print("All done")

    return errors_yaw, errors_xz

def calc_AFD(Experiment_DIR, json_file='result.json', out_dir = 'AFD_output'):
    # Two errors, rotation and translation with precious 3D (x, z and yaw)

    print('out_dir:{}'.format(out_dir))

    with open(json_file, 'r') as f:
        info = json_tricks.load(f)

    files = info['files']
    ref_file = 'ref_init.png'
    ref_file_no_suffix = 'ref_init'

    ref_file = Experiment_DIR + '/' + ref_file

    AFDS = []

    from generate_traj import get_matlab_eng
    eng = get_matlab_eng()
    for file in files[:15]:
        file_no_suffix = os.path.basename(file)[:-4]
        afd = eng.AFD_two_ims_and_save_FDF(Experiment_DIR, ref_file_no_suffix, file_no_suffix, out_dir)
        AFDS.append(afd)

        file = Experiment_DIR+'/'+file_no_suffix+'.png'


        import subprocess
        out_file = out_dir + '/' + file_no_suffix + '_diff.png'
        cmd = 'H:\py_env_conda\py_35_cv_matlab/python pictdiff.py ' + file + ' ' + ref_file + ' ' + out_file

        print(cmd)
        # subprocess.call(['H:\py_env_conda\py_35_cv_matlab/python Experiment1_sub.py', INIT_POSE_STR, delta_pose_STR ], shell=True)
        subprocess.call(cmd, shell=True)


    eng.quit()

    return AFDS


def get_actual_moves():
    ACR_DIR = 'H:/projects/graduation_project_codebase/ACR_experiments/Experiments_DATA/ACR_ZED__EXPERIMENT_1027/'
    #
    Experiment_DIR_S = os.path.join(ACR_DIR, 'ACR_ZED__EXPERIMENT_1028_bookshelf/PnP_Aided/')  #

    from generate_traj import all_experiments
    Experiment_DIR_list = all_experiments(Experiment_DIR_S)

    for Experiment_DIR in Experiment_DIR_list:

        from_experiment_get_actual_moves(Experiment_DIR)

        out_dir = Experiment_DIR + '/' + 'EVAL_output/'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        from generate_traj import from_experiment_get_traj

        actual_move_err_json = out_dir + '/actual_move_error.json'

        from_experiment_get_traj(Experiment_DIR, is_hardware=True, save_json_file=actual_move_err_json)
        three_dof_two_errors(actual_move_err_json)

        AFDS = calc_AFD(Experiment_DIR, json_file=actual_move_err_json, out_dir=out_dir)

        with open(actual_move_err_json, 'r') as f:
            info = json_tricks.load(f)

        info['AFDS'] = AFDS

        with open(actual_move_err_json, 'w') as f:
            json_tricks.dump(info, f, indent=4, sort_keys=True, primitives=True)


def get_AFD_AND_DIFF():

    ACR_DIR = 'H:/projects/graduation_project_codebase/ACR_experiments/Experiments_DATA/ACR_UNREAL_EXPERIMENT_1028_09_sofa_8_close_pnp/'
    Experiment_DIR_S = os.path.join(ACR_DIR, 'PnP_Aided/') #


    from generate_traj import all_experiments
    Experiment_DIR_list = all_experiments(Experiment_DIR_S)

    for Experiment_DIR in Experiment_DIR_list:



        out_dir = Experiment_DIR + '/' + 'EVAL_output/'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        from generate_traj import from_experiment_get_traj

        actual_move_err_json = out_dir + '/afd.json'

        from_experiment_get_traj(Experiment_DIR, is_hardware=False, save_json_file=actual_move_err_json)

        AFDS = calc_AFD(Experiment_DIR, json_file=actual_move_err_json, out_dir=out_dir)

        with open(actual_move_err_json, 'r') as f:
            info = json_tricks.load(f)

        info['AFDS'] = AFDS

        with open(actual_move_err_json, 'w') as f:
            json_tricks.dump(info, f, indent=4, sort_keys=True, primitives=True)

if __name__ == '__main__':
    # ACR_DIR = 'H:/projects/graduation_project_codebase/ACR/'
    # ACR_DIR = 'C:/Code/miaodx/ACR_experiments/ACR/'

    # get_actual_moves()

    get_AFD_AND_DIFF()



