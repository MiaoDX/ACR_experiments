"""
This is for ACR with hardware, we eval accuracy on the movements of the platform
"""

import os
import json_tricks
import numpy as np

def from_experiment_get_actual_moves(DIR='', save_json_file='result.json'):


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

if __name__ == '__main__':
    # ACR_DIR = 'H:/projects/graduation_project_codebase/ACR/'
    ACR_DIR = 'C:/Code/miaodx/ACR_experiments/ACR/'

    Experiment_DIR = os.path.join(ACR_DIR, 'ACR_ZED_OUTPUT/PnP_Aided/20171027_183623/') #
    from_experiment_get_actual_moves(Experiment_DIR)