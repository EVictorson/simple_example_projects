/**
 *  board.cpp
 *
 *  Created on: Aug 17th, 2021
 *     Authors: Eric Victorson <vier0801@gmail.com>
 *        Info: class representing tictactoe board
 *
 */

#include <iostream>
#include <vector>
#include "board.h"

Board::Board(int board_size) : size_{board_size} {
  generate_board();
}

Board::~Board() {
}

void Board::reset_board() {
  for (int row = 0; row < size_; row++) {
    for (int col = 0; col < size_; col++) {
      board_[row][col] = EMPTY_SPACE_;
    }
  }
}

void Board::add_marker(const int &row, const int &col,
                       const std::string &marker) {
  board_[row][col] = marker;
}

bool Board::validate_space_empty(const int &row, const int &col) {
  if (board_[row][col] == EMPTY_SPACE_) {
    return true;
  }
  return false;
}

bool Board::check_for_end_condition() {
  if (check_horizontal_win()) {
    return true;
  } else if (check_vertical_win()) {
    return true;
  } else if (check_positive_diagonal_win()) {
    return true;
  } else if (check_negative_diagonal_win()) {
    return true;
  } else if (check_stalemate()) {
    return true;
  }
  return false;
}

bool Board::check_stalemate() {
  int num_empty_spaces{0};
  for (int row_idx = 0; row_idx < size_; row_idx++) {
    for (int col_idx = 0; col_idx < size_; col_idx++) {
      if (board_[row_idx][col_idx] == EMPTY_SPACE_) {
        num_empty_spaces++;
      }
    }
  }
  if (num_empty_spaces == 0) {
    return true;
  }
  return false;
}

int Board::get_size() {
  return size_;
}

std::string Board::get_element(const int &row, const int &col) {
  return board_[row][col];
}

void Board::generate_board() {
  for (int row = 0; row < size_; row++) {
    std::vector<std::string> row_vec;
    for (int col = 0; col < size_; col++) {
      row_vec.push_back(EMPTY_SPACE_);
    }
  board_.push_back(row_vec);
  }
}

bool Board::check_all_elements_same(const std::vector<std::string> &vec) {
  if (std::equal(vec.begin() + 1, vec.end(), vec.begin())
      && vec[0] != EMPTY_SPACE_) {
    return true;
  }
  return false;
}

bool Board::check_horizontal_win() {
  for (int row_idx = 0; row_idx < size_; row_idx++) {
    if (check_all_elements_same(board_[row_idx])) {
      std::cout << "Horizontal win!" << std::endl;
      return true;
    }
  }
  return false;
}

bool Board::check_vertical_win() {
  for (int col_idx = 0; col_idx < size_; col_idx++) {
    std::vector<std::string> col_vec;
    for (int row_idx = 0; row_idx < size_; row_idx++) {
      col_vec.push_back(board_[row_idx][col_idx]);
    }

    if (check_all_elements_same(col_vec)) {
      std::cout << "Vertical win!" << std::endl;
      return true;
    }
  }
  return false;
}

bool Board::check_positive_diagonal_win() {
  int col_idx = size_ - 1;
  std::vector<std::string> diag_vec;
  for (int row_idx = 0; row_idx < size_; row_idx++) {
    diag_vec.push_back(board_[row_idx][col_idx]);
    col_idx--;
  }
  if (check_all_elements_same(diag_vec)) {
    std::cout << "Positive slope diagonal win!" << std::endl;
    return true;
  }
  return false;
}

bool Board::check_negative_diagonal_win() {
  int col_idx{0};
  std::vector<std::string> diag_vec;
  for (int row_idx = 0; row_idx < size_; row_idx++) {
    diag_vec.push_back(board_[row_idx][col_idx]);
    col_idx++;
  }
  if (check_all_elements_same(diag_vec)) {
    std::cout << "Negative slope diagonal win!" << std::endl;
    return true;
  }

  return false;
}

std::ostream& operator <<(std::ostream& out, const Board &b) {
  out << "\n";
  for (int row_idx = 0; row_idx < b.size_; row_idx++) {
    std::string row_str{""};
    for (int col_idx = 0; col_idx < b.size_; col_idx++) {
      if (col_idx < b.size_ - 1) {
        row_str += b.board_[row_idx][col_idx] + " | ";
      } else {
        row_str += b.board_[row_idx][col_idx];
      }
    }
    out << row_str << "\n";
    std::string horizontal(row_str.length(), '-');
    if (row_idx < b.size_ - 1) {
      out << horizontal << "\n";
    }
  }
  return out;
}
