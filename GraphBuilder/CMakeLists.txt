cmake_minimum_required(VERSION 3.22)
project(SoundSamp)

set(CMAKE_CXX_STANDARD 14)

add_executable(SoundSamp main.cpp dist/jsoncpp.cpp)
