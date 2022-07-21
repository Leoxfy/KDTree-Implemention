#include <iostream>
#include <cstdlib>
#include <vector>

#include "Point.h"
#include "KNN.h"
#include "Naive_KNN.h"
#include "Global_Def.h"
using namespace std;


// 该版本用于二维数据K个邻居测试




vector<Point> test_data_1(){
    vector<Point> training_data;

    training_data.push_back(Point(2,3,0));
    training_data.push_back(Point(4,7,0));
    training_data.push_back(Point(5,4,0));
    training_data.push_back(Point(7,2,0));
    training_data.push_back(Point(8,1,0));
    training_data.push_back(Point(9,6,0));

    return training_data;
}


vector<Point> test_data_2(){
    srand((unsigned)time(NULL));

    vector<Point> training_data;
    for(int i=0;i<num_samples;i++){
        double x = rand()/double(RAND_MAX);
        double y = rand()/double(RAND_MAX);
        int label = rand() % num_classes;
        training_data.push_back(Point(x, y, label));
        //cout<<"["<<x<<", "<<y<<", "<< label <<"],"<<endl;
    }

    return training_data;
}


vector<Point> test_data_3(){
    double data[][3] = {
            {0.328135, 0.891995, 1},
            {0.772759, 0.00997955, 1},
            {0.319346, 0.116886, 1},
            {0.742882, 0.622761, 2},
            {0.204779, 0.473495, 2},
            {0.424482, 0.510727, 2},
            {0.526597, 0.702811, 0},
            {0.411969, 0.0341807, 2},
            {0.673055, 0.0781274, 1},
            {0.864986, 0.44612, 2},
            {0.156468, 0.114353, 1},
            {0.664357, 0.764061, 2},
            {0.579608, 0.493362, 0},
            {0.578631, 0.0167547, 1},
            {0.282723, 0.977538, 2},
            {0.882534, 0.291269, 2},
            {0.0110782, 0.0447401, 2},
            {0.534135, 0.0093997, 0},
            {0.957945, 0.92703, 2},
            {0.544084, 0.28605, 2}
    };
    vector<Point> training_data;
    for(int i=0;i<20;i++){
        training_data.push_back(Point(data[i][0], data[i][1], data[i][2]));
    }
    return training_data;
}

void test1(){
    vector<Point> training_data = test_data_2();

    Point target_point = Point(0, 0, -1);

    cout<<"--------------------------------------"<<endl;

    KNN knn(k);
    knn.set_training_data(training_data);
    knn.train();
    knn.set_test_data(target_point);
    knn.test();

    cout<<"--------------------------------------"<<endl;

    Naive_KNN naive_knn(k);
    naive_knn.set_training_data(training_data);
    naive_knn.train();
    naive_knn.set_test_data(target_point);
    naive_knn.test();

    cout<<"--------------------------------------"<<endl;

    cout<<"本次测试样本个数为:\t"<<training_data.size()<<endl;
    cout<<"使用KD树加速比为:\t"<<naive_knn.test_time/knn.test_time<<endl;

    cout<<"--------------------------------------"<<endl;
}

void test2(){
    vector<Point> training_data;

    training_data.push_back(Point(2,3,0));
    training_data.push_back(Point(4,7,0));
    training_data.push_back(Point(5,4,0));
    training_data.push_back(Point(7,2,0));
    training_data.push_back(Point(8,1,0));
    training_data.push_back(Point(9,6,0));


    KNN knn;
    knn.set_training_data(training_data);
    knn.train();
    knn.test_pre_order();
    cout<<"------------------------------------"<<endl;
    knn.test_in_order();
    cout<<"------------------------------------"<<endl;
    knn.test_post_order();
    cout<<"------------------------------------"<<endl;
    knn.test_level_order();
}

/*
 * k = 1
 * label = 3
 */

int main() {
    test1();
    return 0;
}


