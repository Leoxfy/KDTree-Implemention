//
// Created by 86133 on 2022-07-18.
//

#include "Global_Def.h"
#include "Point.h"

// ������

// ��������: 1)�����پ��� 2)ŷʽ����
int distance_type = 2;

// �������
int num_classes = 3;

// �ھ�����
int k = 7;

// ѵ���������ģ
int num_samples = 1000;




bool cmp_point(const Point a, const Point b){
    return a.distance < b.distance;
}

ostream& operator<<(ostream& os,const Point& point)
{
    os <<"("<<point.x<<", "<<point.y<<")"<< "\t" << point.label <<endl;
    return os;
}

