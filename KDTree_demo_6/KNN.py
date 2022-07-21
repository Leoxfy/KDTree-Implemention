from Node import Node
from Hyperparameters import dimension


class KNN:
    def __init__(self, training_data):
        self.training_data = training_data
        self.kdTree = None
        self.test_data = None
        self.neighbor = None
        self.nearest_distance = float('inf')

    def train(self):
        self.kdTree = self.build_kdtree(0, self.training_data)

    def set_test_data(self, test_data):
        self.test_data = test_data

    def test(self):
        self.get_nearest_neighbor(self.kdTree, self.test_data, 0, None)
        # print(f'KD树最近距离为\t\t{self.nearest_distance}')
        # print('最近邻点为:\t' + str(self.neighbor))

    def get_result(self):
        return self.neighbor.label

    def clear(self):
        self.neighbor = None
        self.test_data = None
        self.nearest_distance = float('inf')
        self.clear_vis(self.kdTree)

    def clear_vis(self, root):
        if root is None:
            return
        if root.visited:
            root.visited = False
        self.clear_vis(root.left_child)
        self.clear_vis(root.right_child)

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

    def get_nearest_neighbor(self, root, target_point, layer, father):
        if root is None:
            if father.visited:
                return

            father.visited = True
            father.root_point.distance = father.root_point.get_distance_to(target_point)

            if father.root_point.distance < self.nearest_distance:
                self.nearest_distance = father.root_point.distance
                self.neighbor = father.root_point

            return

        brother = None

        axis = layer % dimension

        if target_point.data[axis] <= root.root_point.data[axis]:
            brother = root.right_child
            self.get_nearest_neighbor(root.left_child, target_point, layer + 1, root)
        else:
            brother = root.left_child
            self.get_nearest_neighbor(root.right_child, target_point, layer + 1, root)

        mid_distance = abs(root.root_point.data[axis] - target_point.data[axis])

        if mid_distance >= self.nearest_distance:
            pass
        else:
            self.get_nearest_neighbor(brother, target_point, layer + 1, root)

        # 访问根节点
        if root.visited:
            return
        else:
            # 访问当前结点
            root.visited = True
            root.root_point.distance = root.root_point.get_distance_to(target_point)
            if root.root_point.distance < self.nearest_distance:
                self.nearest_distance = root.root_point.distance
                self.neighbor = root.root_point


"""
class Naive_KNN:
    def __init__(self, training_data):
        self.training_data = training_data
        self.test_data = None
        self.neighbor = None
        self.nearest_distance = float('inf')

    def set_test_data(self, target_point):
        self.test_data = target_point

    def get_nearest_neighbor(self):
        for point in self.training_data:
            point.distance = point.get_distance_to(self.test_data)
            if point.distance < self.nearest_distance:
                self.neighbor = point
                self.nearest_distance = point.distance

    def test(self):
        self.get_nearest_neighbor()
        print(f'naive最近距离为\t{self.nearest_distance}')
        print('最近邻点为:\t' + str(self.neighbor))
        self.clear()

    def clear(self):
        self.test_data = None
        self.neighbor = None
        self.nearest_distance = float('inf')
"""
