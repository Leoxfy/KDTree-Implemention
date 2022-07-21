# 该版本提供opencv接口
# 该版本用于演示pixel-wise纹理迁移

from KNN import KNN
from Point import Point
import numpy as np
import time
import cv2


def test_texture_transfer(texture_img_path, content_img_path):
    texture_img = cv2.imread(texture_img_path, 1).astype(np.int_)

    t1 = time.time()

    training_data_list = []
    for i in range(texture_img.shape[0]):
        for j in range(texture_img.shape[1]):
            training_data_list.append(Point([texture_img[i, j, 0], texture_img[i, j, 1], texture_img[i, j, 2]], 0))

    knn = KNN(training_data_list)
    knn.train()

    print('kdtree构建完成')

    content_img = cv2.imread(content_img_path, 1).astype(np.int_)

    # 随机噪音
    content_img = np.random.randint(low=0, high=256, size=(256, 256, 3))

    result_img = np.zeros(shape=content_img.shape, dtype=np.uint8)

    for i in range(content_img.shape[0]):
        for j in range(content_img.shape[1]):
            target_point = Point([content_img[i, j, 0], content_img[i, j, 1], content_img[i, j, 2]], 0)
            knn.set_test_data(target_point)
            knn.test()
            new_pixel = knn.get_result()
            knn.clear()
            result_img[i, j, 0] = new_pixel.data[0]
            result_img[i, j, 1] = new_pixel.data[1]
            result_img[i, j, 2] = new_pixel.data[2]
        print(i)

    t2 = time.time()

    cv2.imwrite('result.png', result_img)

    print('本次生成花费时间：\t' + str(t2-t1) + 's')
    print('纹理图片的大小为：\t' + str(texture_img.shape[0]) + 'x' + str(texture_img.shape[1]))
    print('生成的图片大小为：\t' + str(content_img.shape[0]) + 'x' + str(content_img.shape[1]))
    cv2.imshow('result', result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test_texture_transfer('TestImg/texture_4.jpg', 'TestImg/lena.png')
