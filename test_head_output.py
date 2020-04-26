import numpy as np
import matplotlib.pyplot as plt

def plot_skeleton(keypoints, skeleton):
    """
    :param keypoints: list of keypoints coordinates, from 1 to 17
    :param skeleton: list of keypoints connections
    :return: plot the skeleton
    """
    X = []
    Y = []
    U = []
    V = []
    # convert keypoints to dictionary for easy access
    kp_dict = { i:keypoints[i-1] for i in range(1,18) }
    for joint1, joint2 in skeleton:
        if kp_dict[joint1][2] < 2 or kp_dict[joint2][2] < 2:
            continue
        joint1_xy = np.array(kp_dict[joint1][:2])
        joint2_xy = np.array(kp_dict[joint2][:2])
        offset = joint2_xy - joint1_xy
        X.append(joint1_xy[0])
        Y.append(401-joint1_xy[1])
        U.append(offset[0])
        V.append(-offset[1])
        # U.append(joint2_xy[0])
        # V.append(joint2_xy[1])
    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
    # plt.quiver(X, Y, U, V)
    kp_x_list = [kp[0] for kp in keypoints if kp[2] == 2]
    kp_y_list = [(401-kp[1]) for kp in keypoints if kp[2] == 2]
    plt.scatter(kp_x_list, kp_y_list)
    plt.xlim(0, 401)
    plt.ylim(0, 401)
    plt.show()

def plot_separate_alignment(data, threshold, vflip=True):
    print(np.max(data))
    data[data < threshold] = np.nan
    for i in range(data.shape[0]):
        X, Y = np.meshgrid(np.arange(data.shape[2]), np.arange(data.shape[3]))
        Y = data.shape[3] - Y
        plt.quiver(X, Y, data[i, 0, :, :], (-1) * data[i, 1, :, :], angles='xy', scale_units='xy', scale=1)
        plt.show()

def plot_merged_alignment(data, threshold=0.01, vflip=True):
    data = np.nan_to_num(data)
    # print(np.max(data))
    data[data == 0] = np.nan
    X, Y = np.meshgrid(np.arange(data.shape[2]), np.arange(data.shape[3]))
    Y = data.shape[3] - Y
    for i in range(data.shape[0]):
        plt.quiver(X, Y, data[i, 0, :, :], data[i, 1, :, :]*(-1), angles='xy', scale_units='xy', scale=1)
    plt.show()

def plot_separate_intensity(data, threshold, vflip=True):
    data = np.nan_to_num(data)
    print(np.max(data))
    data[data < threshold] = np.nan
    # X, Y = np.meshgrid(np.arange(data.shape[2]), np.arange(data.shape[3]))
    # Y = data.shape[3] - Y
    for i in range(data.shape[1]):
        print(i)
        # plt.quiver(X, Y, data[i, 0, :, :], data[i, 1, :, :]*(-1), angles='xy', scale_units='xy', scale=1)
        plt.imshow(data[:, i, :, :].reshape(401, 401))
        plt.show()



if __name__ == '__main__':
    # skeleton = [(16, 14), (14, 12), (17, 15), (15, 13), (12, 13), (6, 12), (7, 13), (6, 7), (6, 8), (7, 9), (8, 10), (9, 11), (2, 3), (1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
    # keypoints = [[283.76752 ,141.13904   ,1.     ], [  0.       ,50.        ,0.     ], [289.37875,  136.34225   , 2.     ], [296.59317 ,136.34225   ,2.     ], [  0.,       50.,        0.     ], [286.97394 ,163.52406   ,2.     ], [326.2525  ,172.31818   ,2.     ], [265.33066 ,201.09892   ,2.     ], [  0.       ,50.        ,0.     ], [230.86172 ,220.2861    ,1.     ], [  0. ,      50.,        0.     ], [281.36273 ,245.06952   ,2.     ], [312.62524 ,247.46791   ,2.     ], [262.92584 ,296.2353    ,2.     ], [299.7996  ,296.2353    ,2.     ], [253.30661 ,341.00534   ,2.     ], [291.78357 ,341.8048   , 2.     ]]
    # plot_skeleton(keypoints, skeleton)
    mro_data = np.load("/Users/jiandachen/Projects/pifpaf/openpifpaf/intermediate_results/mid_range_offset_186753.npy")
    plot_merged_alignment(mro_data, 0.01)
