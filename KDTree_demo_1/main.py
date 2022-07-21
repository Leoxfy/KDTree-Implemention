from KNN import KNN
from KNN import Naive_KNN
from KNN import transform
from Node_Point import Point
import numpy as np
import copy


# 该版本用于演示二维数据，选择最近邻居，即K=1

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
    data = np.random.rand(1000, 3)
    return data


def test1():
    # 处理输入数据
    np_data = test_data_2()
    training_data_list = transform(np_data)
    training_data_list_copy = copy.deepcopy(training_data_list)
    target_point = Point(0, 1, None)

    # kd树搜索和可视化
    knn = KNN(training_data_list)
    knn.train()
    # knn.test_in_order()
    knn.set_test_data(target_point)
    knn.test()
    knn.draw_data_distribution()
    knn.print_test_time()
    knn.print_neighbor()

    print('----------------------------------')

    # 暴力搜索和可视化
    naive_knn = Naive_KNN(training_data_list_copy)
    naive_knn.train()
    naive_knn.set_test_data(target_point)
    naive_knn.test()
    naive_knn.draw_data_distribution()
    naive_knn.print_test_time()
    naive_knn.print_neighbor()


if __name__ == '__main__':
    test1()
