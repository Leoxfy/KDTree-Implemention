cmake_minimum_required(VERSION 3.21)
project(KDTree_C_demo_2)

set(CMAKE_CXX_STANDARD 14)

add_executable(
        KDTree_C_demo_2
        main.cpp
        Global_Def.cpp
        Global_Def.h
        KNN.cpp KNN.h
        Naive_KNN.cpp
        Naive_KNN.h
        Node.cpp
        Node.h
        Point.cpp
        Point.h
)
