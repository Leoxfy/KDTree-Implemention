//
// Created by 86133 on 2022-07-18.
//

#include "Global_Def.h"
#include "Point.h"

// 超参数

// 距离类型: 1)曼哈顿距离 2)欧式距离
int distance_type = 2;

// 类别数量
int num_classes = 3;

// 邻居数量
int k = 7;

// 训练集输入规模
int num_samples = 1000;




bool cmp_point(const Point a, const Point b){
    return a.distance < b.distance;
}

ostream& operator<<(ostream& os,const Point& point)
{
    os <<"("<<point.x<<", "<<point.y<<")"<< "\t" << point.label <<endl;
    return os;
}

