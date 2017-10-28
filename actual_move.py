"""
This is for ACR with hardware, we eval accuracy on the movements of the platform
"""

import os
import json_tricks
import numpy as np

def from_experiment_get_actual_moves(DIR='', save_json_file='result.json'):


    actual_moves = []
    move_with_bounding = 0

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

        if int(info['STRATEGY']) > 0:
            move_with_bounding += 1

        actual_moves.append(actual_move)


    print("actual_moves:{}".format(actual_moves))
    print("move_with_bounding:{}".format(move_with_bounding))

    accumulate_move = np.zeros(6)
    for move in actual_moves:
        accumulate_move += move

    print('accumulation move:{}'.format(accumulate_move))

if __name__ == '__main__':
    # ACR_DIR = 'H:/projects/graduation_project_codebase/ACR/'
    ACR_DIR = 'C:/Code/miaodx/ACR_experiments/ACR/'

    Experiment_DIR = os.path.join(ACR_DIR, 'ACR_ZED__EXPERIMENT_1027_statue_10_times/PnP_Aided/20171028_000654/') #
    from_experiment_get_actual_moves(Experiment_DIR)