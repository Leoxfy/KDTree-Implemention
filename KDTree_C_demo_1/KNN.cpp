//
// Created by 86133 on 2022-07-18.
//

#include "KNN.h"
#include <cstdlib>
#include <iostream>
#include <queue>
#include <chrono>
#include <algorithm>
#include <cmath>
#include "Global_Def.h"

using namespace std;
using namespace chrono;





class cmp_x{
public:
    bool operator()(Point a, Point b){
        return a.x < b.x;
    }
};


class cmp_y{
public:
    bool operator()(Point a, Point b){
        return a.y < b.y;
    }
};





KNN::KNN(int K){
    this->K = K;
}


KNN::~KNN(){
    if(kdTree!=NULL){
        destroy_kdTree(kdTree);
    }
}


void KNN::destroy_kdTree(Node*& root){
    if(root==NULL){
        return ;
    }
    destroy_kdTree(root->left_child);
    destroy_kdTree(root->right_child);
    delete root;
}


void KNN::in_order(Node*& root){
    if(root==NULL){
        return ;
    }

    in_order(root->left_child);
    cout << root->root_point ;
    in_order(root->right_child);
}


void KNN::test_in_order(){
    cout<<"kdTree中序遍历结果为:"<<endl;
    this->in_order(this->kdTree);
}


void KNN::pre_order(Node*& root){
    if(root==NULL){
        return ;
    }

    cout << root->root_point ;
    pre_order(root->left_child);
    pre_order(root->right_child);
}


void KNN::test_pre_order() {
    cout<<"kdTree先序遍历结果为:"<<endl;
    pre_order(this->kdTree);
}


void KNN::post_order(Node*& root){
    if(root==NULL){
        return ;
    }

    post_order(root->left_child);
    post_order(root->right_child);
    cout << root->root_point ;
}


void KNN::test_post_order(){
    cout<<"kdTree后序遍历结果为:"<<endl;
    post_order(this->kdTree);
}

void KNN::level_order() const{
    queue<Node*> q;
    q.push(kdTree);
    while(!q.empty()){
        Node* node = q.front();
        q.pop();
        cout<< node->root_point;

        if(node->left_child!=NULL){
            q.push(node->left_child);
        }
        if(node->right_child!=NULL){
            q.push(node->right_child);
        }
    }
}


void KNN::test_level_order() const{
    cout<<"kdTree层序遍历结果为:"<<endl;
    level_order();
}


void KNN::set_training_data(vector<Point>& training){
    this->training_data = training;
}

void KNN::train(){
    kdTree = build_kdTree(1, training_data);
}

Node* KNN::build_kdTree(int layer, vector<Point> &arr){
    if(arr.empty()){
        return NULL;
    }


    if(layer%2==1){
        sort(arr.begin(), arr.end(), cmp_x());
    }else{
        sort(arr.begin(), arr.end(), cmp_y());
    }

    int mid = arr.size() / 2;

    vector<Point> arr_left(arr.begin(), arr.begin()+mid);
    vector<Point> arr_right(arr.begin()+mid+1, arr.end());

    Node *root = new Node(arr.at(mid));

    root->left_child = build_kdTree(layer+1, arr_left);
    root->right_child = build_kdTree(layer+1, arr_right);

    return root;
}


void KNN::set_test_data(Point& point){
    this->test_data = point;
}


void KNN::test(){
    if(this->kdTree==NULL){
        cout<<"请先训练数据。"<<endl;
        return ;
    }
    Node* father = NULL;

    auto start = system_clock::now();
    get_nearest_neighbor(kdTree, test_data, 1, father);
    auto end   = system_clock::now();

    auto duration = duration_cast<microseconds>(end - start);
    this->test_time = double(duration.count()) * microseconds::period::num / microseconds::period::den * 1000;
    print_test_time();
    cout << "kd树上最近距离为\t" << neighbors.front().distance << endl;
    print_neighbors();
    get_test_result();
}




void KNN::print_test_time() const{
    cout << "kd树搜索花费时间\t" << test_time << "ms" << endl;
}

void KNN::print_neighbors(){
    cout << "最近邻点分别为:" << endl;
    for(int i=1;i<=neighbors.size();i++){
        cout << i << ":\t" << neighbors.at(i-1);
    }
}

void KNN::get_test_result(){
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

void KNN::get_nearest_neighbor(Node*& root, Point& target_point, int layer, Node*& father){
    if(root==NULL){
        if(father->visited){
            return ;
        }

        father->visited = true;
        father->root_point.distance = father->root_point.get_distance_to(target_point);

        if(this->neighbors.size() < this->K){
            neighbors.push_back(father->root_point);
            sort(neighbors.begin(), neighbors.end(), cmp_point);
        }else{
            if(father->root_point.distance < neighbors.back().distance){
                neighbors.push_back(father->root_point);
                sort(neighbors.begin(), neighbors.end(), cmp_point);
                neighbors.pop_back();
            }
        }
        return ;
    }


    Node* brother = NULL;

    if(layer%2==1){
        if(target_point.x <= root->root_point.x){
            brother = root->right_child;
            get_nearest_neighbor(root->left_child, target_point, layer+1, root);
        }else{
            brother = root->left_child;
            get_nearest_neighbor(root->right_child, target_point, layer+1, root);
        }
    }else{
        if(target_point.y <= root->root_point.y){
            brother = root->right_child;
            get_nearest_neighbor(root->left_child, target_point, layer+1, root);
        }else{
            brother = root->left_child;
            get_nearest_neighbor(root->right_child, target_point, layer+1, root);
        }
    }


    // 访问兄弟节点
    double mid_distance;
    if(layer%2==1){
        mid_distance = fabs(root->root_point.x - target_point.x);
    }else{
        mid_distance = fabs(root->root_point.y - target_point.y);
    }


    if(mid_distance >= neighbors.back().distance && neighbors.size()==this->K){
        ;
    }else{
        get_nearest_neighbor(brother, target_point, layer+1, root);
    }

    // 访问根节点
    if(root->visited){
        return ;
    }else{
        root->visited = true;

        root->root_point.distance = root->root_point.get_distance_to(target_point);

        if(neighbors.size() < this->K){
            neighbors.push_back(root->root_point);
            sort(neighbors.begin(), neighbors.end(), cmp_point);
        }else{
            if(root->root_point.distance < neighbors.back().distance){
                neighbors.push_back(root->root_point);
                sort(neighbors.begin(), neighbors.end(), cmp_point);
                neighbors.pop_back();
            }
        }
    }
}