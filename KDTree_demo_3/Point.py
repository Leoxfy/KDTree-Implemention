from Hyperparameters import distance_type, dimension


class Point:
    def __init__(self, data_list, label):
        self.data = data_list
        self.label = int(label)
        self.visited = False  # 用于画图
        self.distance = float('inf')  # 用于优先队列保存距离

    # 用于实现优先队列
    def __lt__(self, other):
        return self.distance < other.distance

    def get_distance_to(self, point):
        # 2表示欧式距离, 1表示曼哈顿距离
        distance = 0
        if distance_type == 2:
            for i in range(dimension):
                distance += (self.data[i] - point.data[i]) ** 2
            return distance ** (1/2)
        elif distance_type == 1:
            for i in range(dimension):
                distance += abs(self.data[i] - point.data[i])
            return distance
        else:
            print('请输入正确的距离类型：1)曼哈顿距离;2)欧式距离')
            return None

    def __str__(self):
        if self is None:
            return 'None_Point'
        ans = '('
        for i in range(dimension-1):
            ans += str(round(self.data[i], 2)) + ', '
        ans += str(round(self.data[dimension-1], 2)) + ')'
        ans += '\t' + str(self.label)
        return ans


