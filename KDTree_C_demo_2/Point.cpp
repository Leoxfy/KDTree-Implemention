//
// Created by 86133 on 2022-07-15.
//

#include "Point.h"
#include <iostream>
#include <cmath>
#include "Global_Def.h"

using namespace std;




Point::Point(){}

Point::Point(vector<double>& data, int label):data(data), label(label) {}


double Point::get_distance_to(Point &target_point){
    double ans = 0;
    if(distance_type==2){
        for(int i=0;i<dimension;i++){
            ans += (this->data[i] - target_point.data[i]) * (this->data[i] - target_point.data[i]);
        }
        return sqrt(ans);
    }else if(distance_type==1){
        for(int i=0;i<dimension;i++){
            ans += fabs(this->data[i] - target_point.data[i]);
        }
        return ans;
    }else{
        cout<<"ÇëÊäÈëÕýÈ·µÄ¾àÀëÀàÐÍ£º1)Âü¹þ¶Ù¾àÀë;2)Å·Ê½¾àÀë"<<endl;
    }
    return -1;
}

Point::~Point(){}




