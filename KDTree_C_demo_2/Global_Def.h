//
// Created by 86133 on 2022-07-18.
//


#ifndef KDTREE_C_DEMO_2_GLOBAL_DEF_H
#define KDTREE_C_DEMO_2_GLOBAL_DEF_H


#include "Point.h"
using std::ostream;

class Point;

extern bool cmp_point(const Point& a, const Point& b);

extern ostream& operator<<(ostream& os,const Point& point);

extern int distance_type;

extern int num_classes;

extern int k;

extern int num_samples;

extern int dimension;

#endif //KDTREE_C_DEMO_2_GLOBAL_DEF_H
