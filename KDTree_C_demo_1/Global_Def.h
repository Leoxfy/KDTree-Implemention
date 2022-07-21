//
// Created by 86133 on 2022-07-18.
//


#ifndef KDTREE_GLOBAL_DEF_H
#define KDTREE_GLOBAL_DEF_H


#include "Point.h"

extern bool cmp_point(Point a, Point b);

extern ostream& operator<<(ostream& os,const Point& point);

extern int distance_type;

extern int num_classes;

extern int k;

extern int num_samples;

#endif //KDTREE_GLOBAL_DEF_H
