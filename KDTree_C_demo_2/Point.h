//
// Created by 86133 on 2022-07-15.
//
#pragma once
#ifndef KDTREE_C_DEMO_2_POINT_H
#define KDTREE_C_DEMO_2_POINT_H
#include <iostream>
#include <vector>
#include "Global_Def.h"
using namespace std;

class Point{
public:
    vector<double> data;
    int label{};
    double distance{};

    Point();

    Point(vector<double>& data, int label);

    ~Point();

    double get_distance_to(Point &target_point);
};




#endif //KDTREE_C_DEMO_2_POINT_H
