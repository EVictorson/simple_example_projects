/**
 *  board.h
 *
 *  Created on: Aug 17th, 2021
 *     Authors: Eric Victorson <vier0801@gmail.com>
 *        Info: class representing tictactoe board
 *
 */

#ifndef BOARD_H
#define BOARD_H

#include <vector>
#include <iostream>
#include <string>

class Board {
public:
  Board(int board_size);
  ~Board();

  void reset_board();
  void add_marker(const int &row, const int &col, const std::string &marker);
  bool check_for_end_condition();
  bool check_stalemate();
  bool validate_space_empty(const int &row, const int &col);
  int get_size();

  friend std::ostream& operator <<(std::ostream& out, const Board &b);

protected:
  bool check_horizontal_win();
  bool check_vertical_win();
  bool check_positive_diagonal_win();
  bool check_negative_diagonal_win();
  bool check_all_elements_same(const std::vector<std::string> &vec);
  void generate_board();

  std::vector<std::vector<std::string>> board_;
  int size_;
  const std::string EMPTY_SPACE_{" "};
};

#endif //BOARD_H
