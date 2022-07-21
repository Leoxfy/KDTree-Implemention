//
// Created by 86133 on 2022-07-18.
//

#pragma once
#ifndef KDTREE_KNN_H
#define KDTREE_KNN_H


#include <vector>
#include <map>
#include "Point.h"
#include "Node.h"

using namespace std;

class KNN{
public:
    vector<Point> training_data;
    Node *kdTree;
    double test_time;
    Point test_data;
    int K;
    vector<Point> neighbors;
    map<int,int> neighbor_label_dict;

    KNN(int K=1);

    ~KNN();

    void destroy_kdTree(Node*& root);

    void in_order(Node*& root);

    void test_in_order();

    void pre_order(Node*& root);

    void test_pre_order();

    void post_order(Node*& root);

    void test_post_order();

    void level_order() const;

    void test_level_order() const;

    void set_training_data(vector<Point>& training);

    void train();

    Node* build_kdTree(int layer, vector<Point> &arr);

    void set_test_data(Point& point);

    void test();

    void print_test_time() const;

    void print_neighbors();

    void get_test_result();

    void get_nearest_neighbor(Node*& root, Point& target_point, int layer, Node*& father);

};


#endif //KDTREE_KNN_H
