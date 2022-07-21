//
// Created by 86133 on 2022-07-18.
//
#include "Global_Def.h"
#include "Point.h"
#include <iostream>
using namespace std;
// 超参数
// 维度
int dimension = 4;
// 距离类型: 1)曼哈顿距离 2)欧式距离
int distance_type = 2;
// 类别数量
int num_classes = 3;
// 邻居数量
int k = 7;
// 训练集输入规模
int num_samples = 10000;




bool cmp_point(const Point& a, const Point& b){
    return a.distance < b.distance;
}

ostream& operator<<(ostream& os,const Point& point)
{
    os <<"(";
    for(int i=0;i<dimension-1;i++){
        os << point.data[i] << ", ";
    }
    os << point.data[dimension-1] << ")" <<"\t" << point.label <<endl;
    return os;
}

