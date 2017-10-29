"""
Generate camera trajectory from existing test cases
"""

import json_tricks
import sys
import os
import numpy as np


ACR_DIR = 'H:/projects/graduation_project_codebase/ACR/'
sys.path.append(ACR_DIR)

import utils.Rt_transfrom as Rt_transfrom


def get_matlab_eng():
    """
    # https://cn.mathworks.com/help/matlab/matlab_external/connect-python-to-running-matlab-session.html
    First, convert your MATLAB session to a shared session. From MATLAB call matlab.engine.shareEngine.
    matlab.engine.shareEngine
    """
    import matlab.engine
    m = matlab.engine.find_matlab()
    print('Find matlab at:{}'.format(m))
    print(type(m), m[0])
    eng = matlab.engine.connect_matlab(str(m[0]))
    assert eng.sqrt(4.0) == 2.0
    return eng



# Experiments_DIR = ACR_DIR + '/ACR_UNREAL_EXPERIMENT_1022_23/PnP_Aided/20171022_231729/'



def pose_to_loc_orient(pose):
    # Rt_transfrom.GetEulerDegreeZYX()
    R = Rt_transfrom.EulerZYXDegree2R(pose[3:].reshape(3, 1))  # type: np.ndarray

    print("R:{}\n".format(R))
    d = dict()
    d['loc'] = pose[:3]
    d['orient'] = R
    return d


def from_experiment_get_traj(DIR='', is_hardware=False,save_json_file='result.json'):

    traj = dict()
    pose_path = []
    relative_poses = []
    poses_6D = []
    acutal_moves = []
    files = []

    for i in range(1, 50):
        json_file = os.path.join(DIR, str(i) + '.json')
        if not os.path.isfile(json_file):
            print("All done")
            break

        print(json_file)

        with open(json_file, 'r') as f:
            info = json_tricks.load(f)

        print(info)

        if not 'ref_pose' in traj:
            im_ref_pose = np.array(info['im_ref_pose'])
            traj['im_ref_pose'] = pose_to_loc_orient(im_ref_pose)
            traj['im_ref_pose_6D'] = im_ref_pose
            traj['im_ref_file'] = info['im_ref_file']

        cur_pose = np.array(info['im_cur_pose'])
        relative_pose = np.array(info['relative_pose'])
        if is_hardware:
            acutal_move = np.array(info['acutal_move'])
            acutal_moves.append(acutal_move)

        cur_pose_loc_orient = pose_to_loc_orient(cur_pose)
        pose_path.append(cur_pose_loc_orient)
        poses_6D.append(cur_pose)
        relative_poses.append(relative_pose)

        files.append(info['im_cur_file'])

        traj['num'] = i

    traj['poses'] = pose_path
    traj['poses_6D'] = poses_6D
    traj['relative_poses'] = relative_poses

    traj['files'] = files

    if is_hardware:
        traj['acutal_moves'] = acutal_moves

    with open(save_json_file, 'w') as f:
        # import json
        # json.dump(traj, f, indent=4, sort_keys=True)
        # json.dump(traj, f, indent=4)
        json_tricks.dump(traj, f, indent=4, sort_keys=True, primitives=True)


def all_experiments(Experiments_DIR):
    e_dir_s = []
    for e_dir in os.listdir(Experiments_DIR):
        # e_dir = os.path.realpath(e_dir)
        e_dir_path = os.path.join(Experiments_DIR, e_dir)
        print('DIR:{}'.format(e_dir_path))
        e_dir_s.append(e_dir_path)

    return e_dir_s

if __name__ == '__main__':
    # Experiments_DIR = ACR_DIR + '/ACR_UNREAL_EXPERIMENT/Experiment1_Bisection_HAND/20171023_083727/' # Bisection, hand error
    # Experiments_DIR = ACR_DIR + '/ACR_UNREAL_EXPERIMENT/Experiment1_PnP_Aided_HAND/20171022_231944/'


    Base = 'H:/projects/graduation_project_codebase/ACR_experiments/Experiments_DATA/ACR_UNREAL_EXPERIMENT_1028_09_sofa_8_close_pnp/'

    Experiments_DIR_Bisection = os.path.join(Base, 'Bisection/') #
    Experiments_DIR_PnP = os.path.join(Base, 'PnP_Aided/')  #

    out_dir = 'H:/projects/graduation_project_codebase/ACR_experiments/tmp/'

    dirs_1 = all_experiments(Experiments_DIR_Bisection)
    dirs_2 = all_experiments(Experiments_DIR_PnP)

    assert len(dirs_1) == len(dirs_2)

    choose_num = 10

    # choose_nums = range(len(dirs_1))
    choose_nums = [1]

    for choose_num in choose_nums:

        import os

        eng = get_matlab_eng()
        # eng.draw_traj_fun()

        e_dir_path = dirs_1[choose_num]
        json_file_1 = 'result_1.json'
        from_experiment_get_traj(e_dir_path, save_json_file=json_file_1)



        fig1 = out_dir+'/'+str(choose_num)+'.fig'
        fig2 = out_dir + '/' + str(choose_num) + '_line.fig'

        # eng.draw_traj_fun('json_file', json_file,'start', 15, 'show_num', 30, 'cameraSize', 0.05, 'coor_lim', 0.5, 'present_dir', e_dir)
        eng.draw_traj_fun('json_file', json_file_1, 'start', 1, 'show_num', 7, 'cameraSize', 0.4, 'coor_lim', 10,
                          'present_dir', e_dir_path, 'save_name', fig1, "camera_color", "0 1 0", "line_color", "0 1 0")
        eng.draw_traj_fun('json_file', json_file_1, 'start', 1, 'show_num', 7, 'cameraSize', 0.4, 'coor_lim', 10,
                          'present_dir', e_dir_path, 'Visible', False, 'save_name', fig2, "camera_color", "0 1 0", "line_color", "0 1 0")

        e_dir_path_2 = dirs_2[choose_num]
        json_file_2 = 'result_2.json'
        from_experiment_get_traj(e_dir_path_2, save_json_file=json_file_2)
        fig3 = out_dir+'/'+str(choose_num)+'_pnp.fig'
        fig4 = out_dir + '/' + str(choose_num) + '_line.fig'

        eng.draw_traj_fun('json_file', json_file_2, 'start', 1, 'show_num', 4, 'cameraSize', 0.4, 'coor_lim', 10,
                          'present_dir', e_dir_path, 'save_name', fig3, "camera_color", "1 0 0", 'line_color', "1 0 0" )
        eng.draw_traj_fun('json_file', json_file_2, 'start', 1, 'show_num', 7, 'cameraSize', 0.4, 'coor_lim', 10,
                          'present_dir', e_dir_path, 'Visible', False, 'save_name', fig4, "camera_color", "1 0 0", 'line_color', "1 0 0")


        eng.merge_fig(fig1, fig3)

        eng.quit()

        input('press to continue')

        """
        for e_dir in os.listdir(Experiments_DIR):
            # e_dir = os.path.realpath(e_dir)
            e_dir_path = os.path.join(Experiments_DIR, e_dir)
            print('DIR:{}'.format(e_dir_path))
            input('press to continue')
            from_experiment_get_traj(e_dir_path)
            eng = get_matlab_eng()
            # eng.draw_traj_fun()
            json_file = 'result.json'
            # eng.draw_traj_fun('json_file', json_file,'start', 15, 'show_num', 30, 'cameraSize', 0.05, 'coor_lim', 0.5, 'present_dir', e_dir)
            eng.draw_traj_fun('json_file', json_file, 'start', 1, 'show_num', 8, 'cameraSize', 0.2, 'coor_lim', 35,
                              'present_dir', e_dir, 'save_name', 'tmp/traj.fig')
            eng.draw_traj_fun('json_file', json_file, 'start', 1, 'show_num', 8, 'cameraSize', 0.2, 'coor_lim', 35,
                              'present_dir', e_dir, 'Visible', False, 'save_name', 'tmp/traj_line.fig')
            eng.quit()
        """