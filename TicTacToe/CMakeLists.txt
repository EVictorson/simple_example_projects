cmake_minimum_required(VERSION 3.14)

project(tictactoe)

set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(CMAKE_CXX_STANDARD 17)

include_directories(include)

add_executable(tictactoe
  src/main.cpp
  src/tictactoe.cpp
  src/board.cpp)
