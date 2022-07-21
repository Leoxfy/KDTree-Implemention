//
// Created by 86133 on 2022-07-15.
//
#pragma once
#ifndef KDTREE_POINT_H
#define KDTREE_POINT_H
#include <iostream>
using namespace std;

class Point{
public:
    double x;
    double y;
    int label;
    double distance;

    Point();
    Point(double x, double y, int label);
    double get_distance_to(Point &target_point);
};




#endif //KDTREE_POINT_H
