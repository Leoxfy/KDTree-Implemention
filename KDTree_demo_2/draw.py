from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

"""
该文件用于绘制加速比曲线

k = 1
2的n次方

0.001 0.001 0.001 0.001 0.002 0.001 0.002 0.001 0.001 0.001 0.002 0.002 0.002 0.002 0.002 0.002 0.003 0.003 0.003 0.004 0.003 0.003 0.004 0.008 0.008   0.013   0.012
0.002 0.003 0.002 0.003 0.004 0.006 0.008 0.014 0.023 0.049 0.106 0.138 0.261 0.524 1.064 2.125 4.254 9.300 17.28 37.92 67.34 136.7 272.1 546.4 1098.08 2311.01 5032.46
"""


def draw_1():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    y = [2, 3, 2, 3, 2, 6, 4, 14, 23, 49, 53, 69, 130.5, 262, 532, 1062.5, 1418, 3100, 5760, 9480, 22448, 45592, 68026,
         98300, 137260, 177770, 419372]

    plt.figure(dpi=300)
    plt.plot(x, y, c='orange')
    plt.scatter(x, y, c='orange')
    plt.title('K=1时使用KD树搜索的加速比')
    plt.xlabel(r'数据规模/$2^n$')
    plt.ylabel('加速比')

    plt.show()


def draw_2():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    y1 = [0.001, 0.001, 0.001, 0.001, 0.002, 0.001, 0.002, 0.001, 0.001, 0.001, 0.002, 0.002, 0.002, 0.002, 0.002,
          0.002, 0.003, 0.003, 0.003, 0.004, 0.003, 0.003, 0.004, 0.008, 0.008, 0.013, 0.012]
    y2 = [0.002, 0.003, 0.002, 0.003, 0.004, 0.006, 0.008, 0.014, 0.023, 0.049, 0.106, 0.138, 0.261, 0.524, 1.064,
          2.125, 4.254, 9.300, 17.28, 37.92, 67.34, 136.7, 272.1, 546.4, 1098.08, 2311.01, 5032.46]

    plt.figure(dpi=300)

    plt.plot(x, y2, label='暴力法', c='blue')
    plt.scatter(x, y2, c='blue')

    plt.plot(x, y1, label='KD树加速法', c='orange')
    plt.scatter(x, y1, c='orange')

    plt.ylabel('花费时间/ms')
    plt.xlabel(r'数据规模/$2^n$')
    plt.title('KNN搜索方法时间耗费对比')
    plt.legend()
    plt.show()


def draw_3():
    x = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    y = [67.464, 70.095, 70.813, 75.119, 75.598, 74.401, 73.684, 72.966, 73.205]

    plt.figure(dpi=300)
    plt.plot(x, y, c='orange')
    plt.scatter(x, y, c='orange')
    plt.title('使用不同K值对精度的影响')
    plt.xlabel('K的取值')
    plt.xticks(x)
    plt.ylabel('精度')
    plt.ylim(50, 100)
    plt.show()


if __name__ == '__main__':
    draw_3()