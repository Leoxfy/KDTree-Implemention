from matplotlib import pyplot as plt
import numpy as np
from Point import Point
from Node import Node
import time
from queue import Queue
from Hyperparameters import dimension

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class KNN:
    def __init__(self, training_data, K=1):
        self.training_data = training_data
        self.kdTree = None
        self.test_time = None
        self.test_data = None
        self.neighbors = []
        self.K = K
        self.neighbor_label_dict = {}

    # 训练就是建一颗kdtree
    def train(self):
        self.kdTree = self.build_kdtree(0, self.training_data)

    def set_test_data(self, test_data):
        self.test_data = test_data

    def test(self):
        if self.kdTree is None:
            print('请先训练数据。')
            return
        t1 = time.perf_counter()
        self.get_nearest_neighbor(self.kdTree, self.test_data, 0, None)
        t2 = time.perf_counter()
        self.test_time = (t2 - t1) * 1000
        self.print_test_time()
        print(f'kd树上最近距离为\t{self.neighbors[0].distance}')
        self.print_neighbors()
        self.get_test_result()

    def get_test_result(self):
        for point in self.neighbors:
            if self.neighbor_label_dict.get(str(point.label)) is None:
                self.neighbor_label_dict[str(point.label)] = 1
            else:
                self.neighbor_label_dict[str(point.label)] += 1
        print('邻居字典信息为:\t' + str(self.neighbor_label_dict))
        res = sorted(self.neighbor_label_dict.items(), key=lambda x: x[1], reverse=True)
        print(f'本次分类结果为:\t{res[0][0]}')

    def build_kdtree(self, layer, arr):
        if len(arr) == 0:
            return None

        axis = layer % dimension

        arr.sort(key=lambda obj: obj.data[axis])

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
        print(root.root_point)
        self.in_order(root.right_child)

    def pre_order(self, root):
        if root is None:
            return

        print(root.root_point)
        self.pre_order(root.left_child)
        self.pre_order(root.right_child)

    def post_order(self, root):
        if root is None:
            return

        self.post_order(root.left_child)
        self.post_order(root.right_child)
        print(root.root_point)

    def level_order(self):
        q = Queue()
        q.put(self.kdTree)
        while not q.empty():
            node = q.get()
            print(node.root_point)
            if node.left_child is not None:
                q.put(node.left_child)
            if node.right_child is not None:
                q.put(node.right_child)

    def test_level_order(self):
        print('kdTree层序遍历结果为:')
        self.level_order()

    def test_in_order(self):
        print('kdTree中序遍历结果为:')
        self.in_order(self.kdTree)

    def test_pre_order(self):
        print('kdTree先序遍历结果为:')
        self.pre_order(self.kdTree)

    def test_post_order(self):
        print('kdTree后序遍历结果为:')
        self.post_order(self.kdTree)

    # 画图可以改成中序遍历
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
            # 访问过的话，一定经过了一遍优先队列，所以不需要再过了
            if father.visited:
                return

            father.visited = True  # 剪枝用
            father.root_point.visited = True  # 画图用

            father.root_point.distance = father.root_point.get_distance_to(target_point)
            # 如果列表长度小于K，加入列表
            if len(self.neighbors) < self.K:
                self.neighbors.append(father.root_point)
                self.neighbors.sort()
            # 如果列表长度等于K
            else:  # 和最后一个元素比较，只有distance小才需要加入, 然后丢弃最后一个
                if father.root_point.distance < self.neighbors[-1].distance:
                    self.neighbors.append(father.root_point)
                    self.neighbors.sort()
                    self.neighbors.pop()

            return

        # 递归搜索近似最近点
        # 记录父节点和兄弟节点

        brother = None

        axis = layer % dimension

        # 递归层数为奇数层，对x操作 一定会4选1 进入其中一个分支，然后退出

        if target_point.data[axis] <= root.root_point.data[axis]:
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

        # 当要找K个邻居的时候，列表（优先队列）保留前K个值，
        # 每次计算距离的时候，如果列表（优先队列）没有满，就往列表里面直接加，不需要比较距离
        # 如果列表（优先队列）满了，就比较当前计算出来的距离和列表（优先队列）第3个元素

        # 不可以中序遍历，会出现问题，这里是访问兄弟结点
        # 计算中垂线距离 这里之前忘了加abs

        mid_distance = abs(root.root_point.data[axis] - target_point.data[axis])

        # 这部分逻辑有问题：如果第一次得到的距离和别的都不相交的话，兄弟节点就永远搜索不到
        # 得到垂线距离
        # 和neighbor中最后一位比较，由于已经在回溯了，所以列表必然不为空
        # 如果相交或者neighbors不满K个，才需要搜索兄弟结点
        # 如果既不相交，并且neighbors已经满了K个
        if mid_distance >= self.neighbors[-1].distance and len(self.neighbors) == self.K:
            pass  # 不相交并且 neighbors已满K就直接跳过
        else:  # 相交的话就要进入当前结点的另外一个孩子继续搜索
            self.get_nearest_neighbor(brother, target_point, layer + 1, root)

        # 访问根节点
        if root.visited:
            return
        else:

            # 访问当前结点
            root.visited = True

            # 画图操作使用
            root.root_point.visited = True
            # 对当前结点计算距离
            root.root_point.distance = root.root_point.get_distance_to(target_point)

            if len(self.neighbors) < self.K:
                self.neighbors.append(root.root_point)
                self.neighbors.sort()
            # 如果列表长度等于K
            else:  # 和最后一个元素比较，只有distance小才需要加入, 然后丢弃最后一个
                if root.root_point.distance < self.neighbors[-1].distance:
                    self.neighbors.append(root.root_point)
                    self.neighbors.sort()
                    self.neighbors.pop()

    def print_test_time(self):
        print(f'kd树搜索花费时间\t{self.test_time}ms')

    def print_neighbors(self):
        print('最近邻点分别为:')
        for i, point in enumerate(self.neighbors):
            print(str(i + 1) + ':\t' + str(point))


def transform(training_data: np.ndarray):
    """
    numpy矩阵
    :return: list装的是point
    """
    # 用列表推导式对列表的生成优化
    return [Point(list(training_data[i, :-1]), training_data[i, -1]) for i in range(training_data.shape[0])]


class Naive_KNN:
    def __init__(self, training_data, K=1):
        self.training_data = training_data
        self.test_time = None
        self.test_data = None
        self.neighbors = []
        self.K = K
        self.neighbor_label_dict = {}

    def train(self):
        pass

    def set_test_data(self, target_point):
        self.test_data = target_point

    def get_nearest_neighbor(self):
        for point in self.training_data:
            point.visited = True
            point.distance = point.get_distance_to(self.test_data)
            if len(self.neighbors) < self.K:
                self.neighbors.append(point)
                self.neighbors.sort()
            else:
                if point.distance < self.neighbors[-1].distance:
                    self.neighbors.append(point)
                    self.neighbors.sort()
                    self.neighbors.pop()
        return

    def print_neighbors(self):
        print('最近邻点分别为:')
        for i, point in enumerate(self.neighbors):
            print(str(i + 1) + ':\t' + str(point))

    def test(self):
        if self.training_data is None:
            print('请先训练数据。')
            return
        t1 = time.perf_counter()
        self.get_nearest_neighbor()
        t2 = time.perf_counter()
        self.test_time = (t2 - t1) * 1000
        self.print_test_time()
        print(f'naive最近距离为\t{self.neighbors[0].distance}')
        self.print_neighbors()
        self.get_test_result()

    def get_test_result(self):
        for point in self.neighbors:
            if self.neighbor_label_dict.get(str(point.label)) is None:
                self.neighbor_label_dict[str(point.label)] = 1
            else:
                self.neighbor_label_dict[str(point.label)] += 1
        print('邻居字典信息为:\t' + str(self.neighbor_label_dict))
        res = sorted(self.neighbor_label_dict.items(), key=lambda x: x[1], reverse=True)
        print(f'本次分类结果为:\t{res[0][0]}')

    def print_test_time(self):
        print(f'naive搜索花费时间\t{self.test_time}ms')

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
