cmake_minimum_required(VERSION 3.21)
project(KDTree_C_demo_1)

set(CMAKE_CXX_STANDARD 14)

add_executable(
        KDTree_C_demo_1
        main.cpp
        Point.cpp
        Point.h
        Node.cpp
        Node.h
        KNN.cpp
        KNN.h
        Naive_KNN.cpp
        Naive_KNN.h
        Global_Def.cpp
        Global_Def.h
)
