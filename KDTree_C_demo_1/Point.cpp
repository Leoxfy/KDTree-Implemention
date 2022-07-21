//
// Created by 86133 on 2022-07-15.
//

#include "Point.h"
#include <iostream>
#include <cmath>
#include "Global_Def.h"

using namespace std;




Point::Point() {}
Point::Point(double x, double y, int label):x(x), y(y), label(label) {}


double Point::get_distance_to(Point &target_point){
    if(distance_type==2){
        return sqrt((this->x - target_point.x)*(this->x - target_point.x) + (this->y - target_point.y)*(this->y - target_point.y));
    }else if(distance_type==1){
        return fabs(this->x - target_point.x) + fabs(this->y - target_point.y);
    }else{
        cout<<"ÇëÊäÈëÕýÈ·µÄ¾àÀëÀàÐÍ£º1)Âü¹þ¶Ù¾àÀë;2)Å·Ê½¾àÀë"<<endl;
    }
    return -1;
}




