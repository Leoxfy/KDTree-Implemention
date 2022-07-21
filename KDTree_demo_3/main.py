# 该版本用于演示多维数据选择K个邻居，并进行分类

from KNN import KNN
from KNN import Naive_KNN
from KNN import transform
from Point import Point
import numpy as np
import copy

from Hyperparameters import k, dimension, num_samples, num_classes


# 演示数据1
def test_data_1():
    data = np.array([
        [2, 3, 0],
        [4, 7, 0],
        [5, 4, 0],
        [7, 2, 0],
        [8, 1, 0],
        [9, 6, 0]
    ])
    return data


# 演示大数据情况
def test_data_2():
    data = np.random.rand(num_samples, dimension)
    label = np.random.randint(num_classes, size=(num_samples, 1))
    res = np.concatenate((data, label), axis=1)
    return res


def test_data_3():
    data = np.array([
        [2, 3, 0],
        [4, 7, 0],
        [5, 4, 0],
        [7, 2, 0],
        [8, 1, 0],
        [9, 6, 0],
        # [2, 5, 0]
    ])
    return data


# 这组数据中序遍历会出现问题
def test_data_4():
    data = np.array([
        [0.8, 1.0, 0.2],
        [0.8, 0.2, 0.8],
        [0.9, 0.6, 0.3],
        [0.9, 0.1, 0.0],
        [0.2, 0.0, 0.3],
        [0.0, 0.2, 0.7],
        [0.2, 0.4, 0.6],
        [0.2, 0.6, 0.2],
        [0.8, 0.0, 0.1],
        [0.17, 0.7, 0.4],
        [0.1, 0.6, 0.2],
        [0.9, 0.7, 0.3],
        [0.4, 0.0, 0.9],
        [0.5, 0.1, 0.9],
        [0.3, 0.2, 0.4],
        [0.9, 0.6, 0.0],
        [0.1, 0.8, 0.7],
        [0.4, 1.0, 0.4],
        [1.0, 0.8, 0.9],
        [0.9, 0.1, 0.3],
    ])
    return data


def test_data_5():
    data = np.array([
        [0.328135, 0.891995, 1],
        [0.772759, 0.00997955, 1],
        [0.319346, 0.116886, 1],
        [0.742882, 0.622761, 2],
        [0.204779, 0.473495, 2],
        [0.424482, 0.510727, 2],
        [0.526597, 0.702811, 0],
        [0.411969, 0.0341807, 2],
        [0.673055, 0.0781274, 1],
        [0.864986, 0.44612, 2],
        [0.156468, 0.114353, 1],
        [0.664357, 0.764061, 2],
        [0.579608, 0.493362, 0],
        [0.578631, 0.0167547, 1],
        [0.282723, 0.977538, 2],
        [0.882534, 0.291269, 2],
        [0.0110782, 0.0447401, 2],
        [0.534135, 0.0093997, 0],
        [0.957945, 0.92703, 2],
        [0.544084, 0.28605, 2]
    ])
    return data


def test1():
    # 处理输入数据
    np_data = test_data_2()
    training_data_list = transform(np_data)
    training_data_list_copy = copy.deepcopy(training_data_list)
    list1 = [0] * dimension

    target_point = Point(list1, -1)

    print('--------------------------------------')

    # kd树搜索和可视化
    knn = KNN(training_data_list, K=k)
    knn.train()
    # knn.test_in_order()
    knn.set_test_data(target_point)
    knn.test()
    # knn.draw_data_distribution()

    print('--------------------------------------')

    # 暴力搜索和可视化
    naive_knn = Naive_KNN(training_data_list_copy, K=k)
    naive_knn.train()
    naive_knn.set_test_data(target_point)
    naive_knn.test()
    # naive_knn.draw_data_distribution()

    print('--------------------------------------')

    print(f'本次测试样本个数为:\t{np_data.shape[0]}')
    print(f'使用KD树加速比为:\t{naive_knn.test_time / knn.test_time}')

    print('--------------------------------------')


# 测试前中后层序遍历
def test2():
    np_data = test_data_1()
    training_data_list = transform(np_data)
    knn = KNN(training_data_list, K=k)
    knn.train()
    knn.test_pre_order()
    print('------------------------------------')
    knn.test_in_order()
    print('------------------------------------')
    knn.test_post_order()
    print('------------------------------------')
    knn.test_level_order()


if __name__ == '__main__':
    test1()
