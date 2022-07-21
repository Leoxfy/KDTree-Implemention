//
// Created by 86133 on 2022-07-18.
//
#pragma once
#ifndef KDTREE_C_DEMO_2_NAIVE_KNN_H
#define KDTREE_C_DEMO_2_NAIVE_KNN_H

#include <map>
#include <vector>
#include "Point.h"

using namespace std;
class Naive_KNN{
public:
    vector<Point> training_data;
    Point test_data;
    double test_time{};
    int K;
    vector<Point> neighbors;
    map<int,int> neighbor_label_dict;

    Naive_KNN(int K=1);

    ~Naive_KNN();

    void set_training_data(vector<Point>& training);

    void set_test_data(Point& point);

    void train();

    void get_nearest_neighbor();

    void print_neighbors();

    void test();

    void print_test_time() const;

    void get_test_result();

};


#endif //KDTREE_C_DEMO_2_NAIVE_KNN_H
