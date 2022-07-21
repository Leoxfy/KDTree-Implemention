# 该版本提供opencv接口
# 该版本用于演示mnist手写数字分类

from KNN import KNN
from Point import Point
import numpy as np
import pandas as pd
import time
from matplotlib import pyplot as plt


def transform(training_data: np.ndarray):
    return [Point(list(training_data[i, :-1]), training_data[i, -1]) for i in range(training_data.shape[0])]


def mnist_classification():
    df_train = pd.read_csv('mnist_train.csv')
    np_test = np.array(pd.read_csv('mnist_test.csv'))
    training_data_list = transform(np.array(df_train))
    knn = KNN(training_data_list)
    knn.train()
    print('kd树构建完毕')

    correct = 0
    # np_test.shape[0]
    t1 = time.time()
    for i in range(100):
        target_point = Point(list(np_test[i, :-1]), np_test[i, -1])
        knn.set_test_data(target_point)
        knn.test()
        if target_point.label == knn.get_result():
            correct += 1
        knn.clear()
        print(i)

    t2 = time.time()

    print('本次执行训练集大小为\t60000')
    print('本次执行测试集大小为\t100')
    print('本次执行耗费时间为\t' + str(t2 - t1) + 's')
    print('正确率为\t\t', correct / 100)


def show_demo():
    df_train = pd.read_csv('mnist_train.csv')
    np_test = np.array(pd.read_csv('mnist_test.csv'))
    training_data_list = transform(np.array(df_train))
    knn = KNN(training_data_list)
    knn.train()
    print('kd树构建完毕')

    row = 11
    target_point = Point(list(np_test[row, :-1]), np_test[row, -1])

    img = np_test[row, :-1].reshape(28, 28)

    plt.imshow(img, cmap="gray")
    plt.show()

    knn.set_test_data(target_point)
    knn.test()
    print('ground truth:\t' + str(target_point.label))
    print('预测结果为:    \t' + str(knn.get_result()))
    knn.clear()


if __name__ == '__main__':
    show_demo()
