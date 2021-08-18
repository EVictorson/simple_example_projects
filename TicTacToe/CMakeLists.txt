cmake_minimum_required(VERSION 3.14)

project(tictactoe)

set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(CMAKE_CXX_STANDARD 17)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

include_directories(include)

add_executable(tictactoe
  src/main.cpp
  src/tictactoe.cpp
  src/board.cpp)

enable_testing()

add_executable(board_test
  test/board_test.cpp
  src/board.cpp
)

target_link_libraries(
  board_test
  gtest_main
)

include(GoogleTest)
gtest_discover_tests(board_test)
