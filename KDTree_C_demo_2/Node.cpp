//
// Created by 86133 on 2022-07-18.
//

#include "Node.h"
#include <cstdlib>


Node::Node(Point& root_point){
    this->root_point = root_point;
    this->left_child = NULL;
    this->right_child = NULL;
    this->visited = false;
}