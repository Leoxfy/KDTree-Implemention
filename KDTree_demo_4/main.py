# 该版本用于演示多维数据选择K个邻居，并进行分类
# 该版本提供pandas,numpy,csv接口，供真实数据使用
# 该版本用于演示kaggle测试

from KNN import KNN
from KNN import Naive_KNN
from Point import Point
import numpy as np
import copy
import pandas as pd
from Hyperparameters import k, dimension, num_samples, num_classes


def transform(training_data: np.ndarray):
    """
    numpy矩阵
    :return: list装的是point
    """
    # 用列表推导式对列表的生成优化
    return [Point(list(training_data[i, :-1]), training_data[i, -1]) for i in range(training_data.shape[0])]


# csv接口
def csv_data(file_name):
    df = pd.read_csv(file_name)
    return np.array(df)


# 演示大数据情况
def test_data_2():
    data = np.random.rand(num_samples, dimension)
    label = np.random.randint(num_classes, size=(num_samples, 1))
    res = np.concatenate((data, label), axis=1)
    return res


def test_csv(filename, target_point):
    # 处理输入数据
    np_data = csv_data(filename)
    training_data_list = transform(np_data)
    training_data_list_copy = copy.deepcopy(training_data_list)

    print('--------------------------------------')

    # kd树搜索和可视化
    knn = KNN(training_data_list, K=k)
    knn.train()

    knn.set_test_data(target_point)
    knn.test()

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


def test_1():
    list1 = [0] * dimension
    point = Point(list1, -1)
    test_csv('training_data.csv', point)


def test_kaggle():
    np_train = csv_data('train_1.csv')
    np_test = csv_data('test_1.csv')
    training_data_list = transform(np_train)

    knn = KNN(training_data_list, K=k)
    knn.train()
    file_path = 'my_result_k_' + str(k) + '.csv'
    with open(file_path, mode='w', encoding='utf-8') as file_obj:
        file_obj.write('PassengerId,Survived\n')
        for i in range(np_test.shape[0]):
            p_id = np_test[i, 0]
            test_point = Point(np_test[i, 1:], -1)
            knn.set_test_data(test_point)
            label = knn.test()
            file_obj.write(str(p_id) + ',' + str(label) + '\n')


if __name__ == '__main__':
    test_kaggle()
