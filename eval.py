"""
The evaluation code, 6D for virtual env, 3D (x, z and yaw) for hardware
"""

import numpy as np
import json_tricks
import doctest
import math

def error_position(first, second):
    """
    :param first:
    :param second:
    :return:

    >>> a = [1, 2, 3]
    >>> b = [1, 1, 4]
    >>> abs(error_position(a, b) - math.sqrt(2.0/3)) < 1e-5
    True

    """
    error = (np.array(first) - np.array(second)) ** 2

    return math.sqrt(error.mean())


def six_dof_errors(json_file='result.json'):
    """
    Two errors, rotation and translation with precious 6D
    """

    with open(json_file, 'r') as f:
        info = json_tricks.load(f)

    ref_pose = np.array(info['im_ref_pose_6D']) # type: np.ndarray
    poses = np.array(info['poses_6D']) # type: np.ndarray

    errors = []
    errors_rotation = []
    errors_location = []
    errors_6D = []

    for pose in poses:
        errors.append(error_position(ref_pose, pose))
        errors_rotation.append(error_position(ref_pose[3:], pose[3:]))
        errors_location.append(error_position(ref_pose[:3], pose[:3]))
        errors_6D.append([error_position(ref_pose[0], pose[0]), error_position(ref_pose[1], pose[1]), error_position(ref_pose[2], pose[2]),
                          error_position(ref_pose[3], pose[3]), error_position(ref_pose[4], pose[4]), error_position(ref_pose[5], pose[5])])

    errors = np.array(errors)
    errors_rotation = np.array(errors_rotation)
    errors_location = np.array(errors_location)
    errors_6D = np.array(errors_6D)

    print("error_postion:{}\nerror_rotation:{}\nerrors_location:{}".format(errors.T, errors_rotation.T, errors_location.T))
    print("All done")

    return errors, errors_rotation, errors_location, errors_6D

def three_dof_two_errors(json_file='result.json'):
    """
    Two errors, rotation and translation with precious 3D (x, z and yaw)
    """

    with open(json_file, 'r') as f:
        info = json_tricks.load(f)

    ref_pose = np.array(info['im_ref_pose_6D']) # type: np.ndarray
    start_pose = np.array(info['poses_6D'])[0] # type: np.ndarray

    target_movement = ref_pose - start_pose

    print("ref_pose:{}\n start_pose:{}\n target_movement:{}".format(ref_pose, start_pose, target_movement))

    relative_poses = np.array(info['relative_poses'])

    errors_yaw = []
    errors_xz = []

    relative_poses = np.insert(relative_poses, 0, np.zeros(6), axis=0) # for calc the init error

    now_movement = np.zeros(6)
    for move in relative_poses:

        move[:3] = -move[:3] # note the minus, for translation
        now_movement += move

        errors_yaw.append(error_position(target_movement[4], now_movement[4]))
        errors_xz.append(error_position([target_movement[0], target_movement[2]], [now_movement[0], now_movement[2]]))

    errors_yaw = np.array(errors_yaw)
    errors_xz = np.array(errors_xz)


    print("errors_yaw:{}\nerrors_xz:{}".format(errors_yaw.T, errors_xz.T))

    print('All num:{}, len(errors):{}'.format(info['num'], len((errors_yaw))))
    print("All done")

if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    doctest.testmod()

    # six_dof_two_errors('result.json')
    three_dof_two_errors('result.json')