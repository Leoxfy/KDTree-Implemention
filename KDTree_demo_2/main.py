# 该版本用于演示二维数据选择K个邻居，并进行分类

from KNN import KNN
from KNN import Naive_KNN
from KNN import transform
from Node_Point import Point
import numpy as np
import copy

# 超参数
k = 1


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
    num_samples = 1000
    data = np.random.rand(num_samples, 2)
    label = np.random.randint(3, size=(num_samples, 1))
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


def test1():
    # 处理输入数据
    np_data = test_data_2()
    training_data_list = transform(np_data)
    training_data_list_copy = copy.deepcopy(training_data_list)
    target_point = Point(1, 1, -1)

    print('--------------------------------------')

    # kd树搜索和可视化
    knn = KNN(training_data_list, K=k)
    knn.train()
    # knn.test_in_order()
    knn.set_test_data(target_point)
    knn.test()
    knn.draw_data_distribution()

    print('--------------------------------------')

    # 暴力搜索和可视化
    naive_knn = Naive_KNN(training_data_list_copy, K=k)
    naive_knn.train()
    naive_knn.set_test_data(target_point)
    naive_knn.test()
    naive_knn.draw_data_distribution()

    print('--------------------------------------')

    print(f'本次测试样本个数为:\t{np_data.shape[0]}')
    print(f'使用KD树加速比为:\t{naive_knn.test_time/knn.test_time}')

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
