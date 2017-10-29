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




if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    doctest.testmod()

    # six_dof_two_errors('result.json')
