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
    d['loc'] = pose[3:]
    d['orient'] = R
    return d


def from_experiment_get_traj(DIR='', save_json_file='result.json'):

    traj = dict()
    pose_path = []
    relative_poses = []
    poses_6D = []

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

        cur_pose = np.array(info['im_cur_pose'])
        relative_pose = np.array(info['relative_pose'])

        cur_pose_loc_orient = pose_to_loc_orient(cur_pose)
        pose_path.append(cur_pose_loc_orient)
        poses_6D.append(cur_pose)
        relative_poses.append(relative_pose)

        traj['num'] = i

    traj['poses'] = pose_path
    traj['poses_6D'] = poses_6D
    traj['relative_poses'] = relative_poses

    with open(save_json_file, 'w') as f:
        # import json
        # json.dump(traj, f, indent=4, sort_keys=True)
        # json.dump(traj, f, indent=4)
        json_tricks.dump(traj, f, indent=4, sort_keys=True, primitives=True)

if __name__ == '__main__':
    # Experiments_DIR = ACR_DIR + '/ACR_UNREAL_EXPERIMENT/Experiment1_Bisection_HAND/20171023_083727/' # Bisection, hand error
    # Experiments_DIR = ACR_DIR + '/ACR_UNREAL_EXPERIMENT/Experiment1_PnP_Aided_HAND/20171022_231944/'

    Experiments_DIR = os.path.join(ACR_DIR, 'ACR_UNREAL_EXPERIMENT_1024_14/Bisection/') #
    # Experiments_DIR = os.path.join(ACR_DIR, 'ACR_UNREAL_EXPERIMENT/Experiment1_PnP_Aided_HAND/')  #


    import os
    for e_dir in os.listdir(Experiments_DIR):
        # e_dir = os.path.realpath(e_dir)
        e_dir_path = os.path.join(Experiments_DIR, e_dir)
        print('DIR:{}'.format(e_dir_path))
        input('press to continue')
        from_experiment_get_traj(e_dir_path)
        eng = get_matlab_eng()
        # eng.draw_traj_fun()
        json_file = 'result.json'
        eng.draw_traj_fun('json_file', json_file,'start', 15, 'show_num', 30, 'cameraSize', 0.05, 'coor_lim', 0.5, 'present_dir', e_dir)
        # eng.draw_traj_fun('json_file', json_file, 'start', 1, 'show_num', 2, 'cameraSize', 0.2, 'coor_lim', 2,
        #                   'present_dir', e_dir)
        eng.quit()