from matplotlib import pyplot as plt
import numpy as np
from Node_Point import Point
from Node_Point import Node
import time

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class KNN:
    def __init__(self, training_data):
        self.training_data = training_data
        self.kdTree = None
        self.nearest_distance = float('inf')
        self.test_time = None
        self.test_data = None
        self.neighbor_list = [None]

    # 训练就是建一颗kdtree
    def train(self):
        self.kdTree = self.build_kdtree(1, self.training_data)

    def set_test_data(self, test_data):
        self.test_data = test_data

    def test(self):
        if self.kdTree is None:
            print('请先训练数据。')
            return
        t1 = time.perf_counter()
        self.get_nearest_neighbor(self.kdTree, self.test_data, 1, None)
        t2 = time.perf_counter()
        self.test_time = (t2 - t1) * 1000
        print(f'kd树上最近距离为{self.nearest_distance}')

    def build_kdtree(self, layer, arr):
        if len(arr) == 0:
            return None

        if layer % 2 == 1:
            # 递归层数为奇数层，对x排序
            # 可以换成线性时间选择
            arr.sort(key=lambda obj: obj.x)
        else:
            arr.sort(key=lambda obj: obj.y)

        mid = len(arr) // 2
        # 建树
        arr_left = arr[:mid]
        arr_right = arr[mid + 1:]

        root = Node(arr[mid])
        root.left_child = self.build_kdtree(layer + 1, arr_left)
        root.right_child = self.build_kdtree(layer + 1, arr_right)
        return root

    def in_order(self, root):
        if root is None:
            return

        self.in_order(root.left_child)
        print(root.root_point.x, ',', root.root_point.y)
        self.in_order(root.right_child)

    def test_in_order(self):
        self.in_order(self.kdTree)

    def draw_data_distribution(self):
        x_not_visited = []
        y_not_visited = []
        x_visited = []
        y_visited = []
        plt.figure(dpi=300)

        # 没访问的加入
        for point in self.training_data:
            if not point.visited:
                x_not_visited.append(point.x)
                y_not_visited.append(point.y)
            else:
                x_visited.append(point.x)
                y_visited.append(point.y)

        plt.scatter(x_not_visited, y_not_visited, c='blue', label='未访问的结点')
        plt.scatter(x_visited, y_visited, c='red', label='访问过的结点')
        plt.scatter(self.test_data.x, self.test_data.y, marker='*', c='green', s=150, label='测试点')
        plt.title('使用KD树进行K近邻搜索的数据分布')
        plt.legend()
        plt.show()

    def get_nearest_neighbor(self, root, target_point, layer, father):
        # 结束条件
        if root is None:
            # 走到叶子结点了
            # print('找到叶子结点', ',父结点为', father.root_point.x, ',', father.root_point.y)
            # 还需要比较当前距离和最近距离的大小，并且更新
            if father.visited:
                return

            father.visited = True
            father.root_point.visited = True
            distance = target_point.get_distance_to(father.root_point)
            if distance < self.nearest_distance:
                self.nearest_distance = distance
                self.neighbor_list[0] = father.root_point
                # print('叶子结点更新')
            return

        # 递归搜索近似最近点
        # 记录父节点和兄弟节点
        brother = None
        if layer % 2 == 1:
            # 递归层数为奇数层，对x操作 一定会4选1 进入其中一个分支，然后退出
            if target_point.x <= root.root_point.x:
                brother = root.right_child
                self.get_nearest_neighbor(root.left_child, target_point, layer + 1, root)
            else:
                brother = root.left_child
                self.get_nearest_neighbor(root.right_child, target_point, layer + 1, root)
        else:
            # 递归层数为偶数层，对y操作
            if target_point.y <= root.root_point.y:
                brother = root.right_child
                self.get_nearest_neighbor(root.left_child, target_point, layer + 1, root)
            else:
                brother = root.left_child
                self.get_nearest_neighbor(root.right_child, target_point, layer + 1, root)

        # 回溯: 向上找父节点，如果当前最近圆和父节点不相交，继续向上回溯
        # 如果当前最近圆和父节点相交，就到父节点的另外一个孩子结点找最最近圆
        # 考虑标记问题，我在搜索另外一个孩子结点，可能最近圆又和父节点相交，这样就死循环了，所以一定要标记
        # 如何标记呢？在进入另外一个孩子之前，标记父节点，或者说，回溯到上一层，先判断这一层有没有标记，
        # 如果有标记，就忽略这层的逻辑，直接再向上回溯
        # 如果没有标记，进入这一层的逻辑，先标记，然后，再判断是否相交，做相交的一套逻辑

        # 计算中垂线距离
        if layer % 2 == 1:  # 对x操作
            mid_distance = abs(root.root_point.x - target_point.x)
        else:  # 对y操作
            mid_distance = abs(root.root_point.y - target_point.y)

        # 得到垂线距离
        if mid_distance >= self.nearest_distance:
            pass  # 相切或者相离就直接跳过
        else:  # 相交的话就要进入当前结点的另外一个孩子继续搜索
            self.get_nearest_neighbor(brother, target_point, layer + 1, root)

        if root.visited:
            return
        else:
            root.visited = True

            # 画图操作使用
            root.root_point.visited = True
            # 对当前结点计算距离
            distance = target_point.get_distance_to(root.root_point)
            if distance < self.nearest_distance:
                self.nearest_distance = distance
                self.neighbor_list[0] = root.root_point
                # print('中间结点更新')

    def print_test_time(self):
        print(f'kd树搜索花费时间{self.test_time}s')

    def print_neighbor(self):
        print('最近邻点为', self.neighbor_list[0])


def transform(training_data: np.ndarray):
    """
    numpy矩阵
    :return: list装的是point
    """
    # 用列表推导式对列表的生成优化
    return [Point(training_data[i, 0], training_data[i, 1], training_data[i, 2]) for i in range(training_data.shape[0])]
    # m = training_data.shape[0]
    # data_list = []
    # for i in range(m):
    #     x = training_data[i, 0]
    #     y = training_data[i, 1]
    #     label = training_data[i, 2]
    #     data_list.append(Point(x, y, label))
    #
    # return data_list


class Naive_KNN:
    def __init__(self, training_data):
        self.training_data = training_data
        self.nearest_distance = float('inf')
        self.test_time = None
        self.test_data = None
        self.neighbor_list = [None]

    def train(self):
        pass

    def set_test_data(self, target_point):
        self.test_data = target_point

    def get_nearest_neighbor(self):
        for point in self.training_data:
            point.visited = True
            distance = self.test_data.get_distance_to(point)
            if distance < self.nearest_distance:
                self.neighbor_list[0] = point
                self.nearest_distance = distance
        return

    def print_neighbor(self):
        print('最近邻点为', self.neighbor_list[0])

    def test(self):
        if self.training_data is None:
            print('请先训练数据。')
            return
        t1 = time.perf_counter()
        self.get_nearest_neighbor()
        t2 = time.perf_counter()
        self.test_time = (t2 - t1) * 1000
        print(f'naive搜索最近距离为{self.nearest_distance}')

    def print_test_time(self):
        print(f'naive搜索花费时间{self.test_time}s')

    def draw_data_distribution(self):
        x_not_visited = []
        y_not_visited = []
        x_visited = []
        y_visited = []
        plt.figure(dpi=300)

        # 没访问的加入
        for point in self.training_data:
            if not point.visited:
                x_not_visited.append(point.x)
                y_not_visited.append(point.y)
            else:
                x_visited.append(point.x)
                y_visited.append(point.y)

        plt.scatter(x_not_visited, y_not_visited, c='blue', label='未访问的结点')
        plt.scatter(x_visited, y_visited, c='red', label='访问过的结点')
        plt.scatter(self.test_data.x, self.test_data.y, marker='*', c='green', s=150, label='测试点')
        plt.title('使用暴力方法进行K近邻搜索的数据分布')
        plt.legend()
        plt.show()
