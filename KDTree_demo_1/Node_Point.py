# 超参数设置: 2表示欧式距离, 1表示曼哈顿距离
distance_type = 2


class Point:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label
        self.visited = False  # 用于画图

    def get_distance_to(self, point):
        # 2表示欧式距离, 1表示曼哈顿距离
        if distance_type == 2:
            return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** (1 / 2)
        elif distance_type == 1:
            return abs(self.x - point.y) + abs(self.y - point.y)
        else:
            print('请输入正确的距离类型：1)曼哈顿距离;2)欧式距离')
            return None

    def __str__(self):
        if self is None:
            return 'None_Point'
        return "(%.2f, %.2f)" % (self.x, self.y)


class Node:
    def __init__(self, point):
        self.root_point = point
        self.left_child = None
        self.right_child = None
        self.visited = False

    # def __str__(self):
    #     if self.root_point is None:
    #         print('Node_None')
    #     print(self.root_point)
