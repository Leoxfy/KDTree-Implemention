//
// Created by 86133 on 2022-07-18.
//
#pragma once
#ifndef KDTREE_NODE_H
#define KDTREE_NODE_H

#include "Point.h"

class Node{
public:
    Point root_point;
    Node *left_child;
    Node *right_child;
    bool visited = false;


    Node(Point& root_point);
};


#endif //KDTREE_NODE_H
