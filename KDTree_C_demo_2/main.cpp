#include <iostream>
#include <cstdlib>
#include <vector>

#include "Point.h"
#include "KNN.h"
#include "Naive_KNN.h"
#include "Global_Def.h"
using namespace std;


// 该版本用于多维数据K个邻居测试




vector<Point> test_data_1(){
    vector<Point> training_data;

    vector<double>p1 = {2, 3};
    vector<double>p2 = {4, 7};
    vector<double>p3 = {5, 4};
    vector<double>p4 = {7, 2};
    vector<double>p5 = {8, 1};
    vector<double>p6 = {9, 6};
    training_data.emplace_back(Point(p1,0));
    training_data.emplace_back(Point(p2,0));
    training_data.emplace_back(Point(p3,0));
    training_data.emplace_back(Point(p4,0));
    training_data.emplace_back(Point(p5,0));
    training_data.emplace_back(Point(p6,0));


    return training_data;
}


vector<Point> test_data_2(){
    srand((unsigned)time(NULL));

    vector<Point> training_data;
    for(int i=0;i<num_samples;i++){
        vector<double> data;
        for(int j=0;j<dimension;j++){
            double x = rand()/double(RAND_MAX);
            data.emplace_back(x);
        }
        int label = rand() % num_classes;
        training_data.emplace_back(data, label);
    }

    return training_data;
}


vector<Point> test_data_3(){

    vector<double>p1 = {0.328135, 0.891995};
    vector<double>p2 = {0.772759, 0.00997955};
    vector<double>p3 = {0.319346, 0.116886};
    vector<double>p4 = {0.742882, 0.622761};
    vector<double>p5 = {0.204779, 0.473495};
    vector<double>p6 = {0.424482, 0.510727};
    vector<double>p7 = {0.526597, 0.702811};
    vector<double>p8 = {0.411969, 0.0341807};
    vector<double>p9 = {0.673055, 0.0781274};
    vector<double>p10 = {0.864986, 0.44612};
    vector<double>p11 = {0.156468, 0.114353};
    vector<double>p12 = {0.664357, 0.764061};
    vector<double>p13 = {0.579608, 0.493362};
    vector<double>p14 = {0.578631, 0.0167547};
    vector<double>p15 = {0.282723, 0.977538};
    vector<double>p16 = {0.882534, 0.291269};
    vector<double>p17 = {0.0110782, 0.0447401};
    vector<double>p18 = {0.534135, 0.0093997};
    vector<double>p19 = {0.957945, 0.92703};
    vector<double>p20 = {0.544084, 0.28605};

    vector<Point> training_data;
    training_data.emplace_back(Point(p1,1));
    training_data.emplace_back(Point(p2,1));
    training_data.emplace_back(Point(p3,1));
    training_data.emplace_back(Point(p4,2));
    training_data.emplace_back(Point(p5,2));
    training_data.emplace_back(Point(p6,2));
    training_data.emplace_back(Point(p7,0));
    training_data.emplace_back(Point(p8,2));
    training_data.emplace_back(Point(p9,1));
    training_data.emplace_back(Point(p10,2));
    training_data.emplace_back(Point(p11,1));
    training_data.emplace_back(Point(p12,2));
    training_data.emplace_back(Point(p13,0));
    training_data.emplace_back(Point(p14,1));
    training_data.emplace_back(Point(p15,2));
    training_data.emplace_back(Point(p16,2));
    training_data.emplace_back(Point(p17,2));
    training_data.emplace_back(Point(p18,0));
    training_data.emplace_back(Point(p19,2));
    training_data.emplace_back(Point(p20,2));
    return training_data;
}


void test1(){
    vector<Point> training_data = test_data_2();

    vector<double> t_data;
    for(int i=0;i<dimension;i++){
        t_data.emplace_back(0);
    }
    Point target_point = Point(t_data, -1);

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
    cout<<"本次选择邻居数量为:\t"<<k<<endl;
    cout<<"使用KD树加速比为:\t"<<naive_knn.test_time/knn.test_time<<endl;

    cout<<"--------------------------------------"<<endl;
}


// 测试前中后层序遍历
void test2(){
    vector<Point> training_data = test_data_1();
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


int main() {
    test1();
    return 0;
}


