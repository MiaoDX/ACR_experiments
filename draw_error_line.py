


def draw_errors_list(errors_list, name='rotation error', ylabel='Error(°)'):
    import matplotlib.pyplot as plt

    x = range(1, 20)

    for errors in errors_list:
        plt.plot(range(1, len(errors)+1), errors) #, marker='x'

    # plt.xlim([0, 10])
    # plt.ylim([0, 30])
    plt.xlabel('i(iteration)')
    plt.ylabel(ylabel)
    # plt.title(name)
    # plt.legend([errors], loc='upper left')

    plt.show()



def draw_error_line(Experiments_DIR, is_unreal=True):
    import os

    from generate_traj import all_experiments

    dirs = all_experiments(Experiments_DIR)

    errors_rotation_list = []
    errors_location_list = []


    for e_dir in dirs:

        out_dir = e_dir + '/EVAL_output/'

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        json_file = out_dir + '/actual_move_error_only.json'


        from generate_traj import from_experiment_get_traj


        if is_unreal:
            from_experiment_get_traj(e_dir, is_hardware=False, save_json_file=json_file)
            from eval import six_dof_errors
            errors, errors_rotation, errors_location, errors_6D = six_dof_errors(json_file)
            errors_rotation_list.append(errors_rotation)
            errors_location_list.append(errors_location)
        else:
            from_experiment_get_traj(e_dir, is_hardware=True, save_json_file=json_file)
            from actual_move import three_dof_two_errors

            errors_yaw, errors_xz = three_dof_two_errors(json_file)

            errors_rotation_list.append(errors_yaw)
            errors_location_list.append(errors_xz)


    last_rotations = []
    last_locations = []

    for i in range(len(errors_location_list)):
        last_rotations.append(errors_rotation_list[i][-1])
        last_locations.append(errors_location_list[i][-1])

    print("The last number of errors_rotation_list:{}".format(last_rotations))
    print("                   errors_location_list:{}".format(last_locations))

    input('press to continue')
    draw_errors_list(errors_rotation_list)
    draw_errors_list(errors_location_list, name='location error', ylabel='Error(cm)')




if __name__ == '__main__':
    import os

    ACR_DIR = 'H:/projects/graduation_project_codebase/ACR_experiments/Experiments_DATA/'

    # Hardware = os.path.join(ACR_DIR, 'ACR_ZED_1028_10_again/PnP_Aided/') #
    #
    # draw_error_line(Hardware, False)


    Unreal = os.path.join(ACR_DIR, 'ACR_UNREAL_EXPERIMENT_1028_09_sofa_8_close_pnp/PnP_Aided/')

    draw_error_line(Unreal, True)


