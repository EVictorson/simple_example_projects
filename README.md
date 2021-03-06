# Simple Example Projects

![CMake and Test](https://github.com/EVictorson/simple_example_projects/actions/workflows/cmake.yml/badge.svg)
![Languages](https://img.shields.io/github/languages/count/evictorson/simple_example_projects)
![Last Commit](https://img.shields.io/github/last-commit/evictorson/simple_example_projects)
![](https://img.shields.io/github/commits-since/evictorson/simple_example_projects/v0.1-alpha)
![](https://img.shields.io/github/issues/evictorson/simple_example_projects)
![](https://img.shields.io/github/license/evictorson/simple_example_projects)

### Projects
Currently the only project directory is for playing Tic-Tac-Toe.  Others may be added at a later time.  

### Setup
In the root of the project directory (there is only TicTacToe currently) create a `/build` and `/bin` directory.  
Inside of `/build` run `cmake ..` followed by `make`.    
To easily run tests use `make test`.  
Then, execute the compiled binary in the `/bin` directory.

### Linters
Preferred linters are pylint and cpplint.  

### Dependencies
The C++ testing framework depends on GTest.
