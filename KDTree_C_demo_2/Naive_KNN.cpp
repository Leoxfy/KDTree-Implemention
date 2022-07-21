//
// Created by 86133 on 2022-07-18.
//

#include "Naive_KNN.h"
#include "Global_Def.h"
#include <iostream>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace chrono;




Naive_KNN::Naive_KNN(int K){
    this->K = K;
}
Naive_KNN::~Naive_KNN()= default;

void Naive_KNN::set_training_data(vector<Point>& training){
    this->training_data = training;
}

void Naive_KNN::set_test_data(Point& point){
    this->test_data = point;
}

void Naive_KNN::train(){
    ;
}

void Naive_KNN::get_nearest_neighbor(){
    for(Point& point: training_data){
        point.distance = point.get_distance_to(test_data);
        if(neighbors.size() < this->K){
            neighbors.push_back(point);
            sort(neighbors.begin(), neighbors.end(), cmp_point);
        }else{
            if(point.distance < neighbors.back().distance){
                neighbors.push_back(point);
                sort(neighbors.begin(), neighbors.end(), cmp_point);
                neighbors.pop_back();
            }
        }
    }
}

void Naive_KNN::print_neighbors(){
    cout << "最近邻点分别为:" << endl;
    for(int i=1;i<=neighbors.size();i++){
        cout << i << ":\t" << neighbors.at(i-1);
    }
}

void Naive_KNN::test(){
    if(this->training_data.empty()){
        cout<<"请先训练数据。"<<endl;
        return ;
    }

    auto start = system_clock::now();
    get_nearest_neighbor();
    auto end   = system_clock::now();

    auto duration = duration_cast<microseconds>(end - start);
    this->test_time = double(duration.count()) * microseconds::period::num / microseconds::period::den * 1000;
    print_test_time();
    cout << "naive最近距离为\t\t" << neighbors.front().distance << endl;
    print_neighbors();
    get_test_result();
}

void Naive_KNN::print_test_time() const{
    cout << "naive搜索花费时间\t" << test_time << "ms" << endl;
}

void Naive_KNN::get_test_result(){
    for(auto & neighbor : neighbors){
        if(neighbor_label_dict.find(neighbor.label)==neighbor_label_dict.end()){
            neighbor_label_dict.insert(pair<int, int>(neighbor.label,1));
        }else{
            neighbor_label_dict[neighbor.label]++;
        }
    }
    cout << "邻居字典信息为:\t{";
    int max_cnt = INT_MIN;
    int label = -1;
    for(auto & it : neighbor_label_dict){
        cout<< "'" << it.first << "':" << it.second << ", ";
        if(it.second > max_cnt){
            max_cnt = it.second;
            label = it.first;
        }
    }
    cout<< "}" << endl;
    cout<< "本次分类结果为:\t'" << label << "'" <<endl;
}