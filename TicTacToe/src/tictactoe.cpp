/**
 *  tictactoe.cpp
 *
 *  Created on: Aug 17th, 2021
 *     Authors: Eric Victorson <vier0801@gmail.com>
 *        Info: class handling tictactoe gameplay
 *
 */

#include <iostream>
#include <vector>
#include "board.h"
#include "tictactoe.h"

TicTacToe::TicTacToe() {
  int board_size = display_startup_message();
  board_ = std::make_unique<Board>(board_size);
}

TicTacToe::~TicTacToe() {
}

void TicTacToe::run() {
  bool replay = true;
  while (replay) {
    board_->reset_board();
    std::cout << *board_ << std::endl;
    while (!board_->check_for_end_condition()) {
      get_user_input();
      toggle_player_num();
      std::cout << *board_ << std::endl;
    }
    if (!board_->check_stalemate()) {
      std::cout << "Player " << !current_player_ + 1;
      std::cout << " has won!" << std::endl;
    }
    replay = check_for_replay();
  }
}

int TicTacToe::get_current_player() {
  return current_player_;
}

int TicTacToe::display_startup_message() {
  int board_size;

  std::cout << "Welcome to TicTacToe!" << std::endl;
  std::cout << "Please enter the size of the TicTacToe board: ";
  std::cin >> board_size;
  while (std::cin.fail()) {
      std::cout << "\nThe board size must be an integer." << std::endl;
      std::cout << "Please enter an integer size: ";
      std::cin.clear();
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      std::cin >> board_size;
  }

  return board_size;
}

void TicTacToe::get_user_input() {
  bool space_empty = false;
  int row_input;
  int col_input;

  std::cout << "Player " << current_player_ + 1 << ": " << std::endl;
  while (!space_empty) {
    std::cout << "Enter the row you would like to place a marker in: \n";
    row_input = get_and_validate_input();

    std::cout << "Enter the column you would like to place a marker in: \n";
    col_input = get_and_validate_input();

    space_empty = board_->validate_space_empty(row_input, col_input);
    if (!space_empty) {
      std::cout << "That space is taken!  Please enter an empty space.\n";
    }
  }
  board_->add_marker(row_input, col_input, PLAYER_SYMBOLS_[current_player_]);
}

int TicTacToe::get_and_validate_input() {
  int val;
  int board_size = board_->get_size();

  std::cin >> val;
  while (std::cin.fail() || val >= board_size) {
    std::cout << "\nIndex must be an integer > 0 and less than ";
    std::cout << board_size << "." << std::endl;
    std::cout << "Please re-enter a value: ";
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cin >> val;
  }
  return val;
}

void TicTacToe::toggle_player_num() {
  current_player_ = !current_player_;
}

bool TicTacToe::check_for_replay() {
  std::string user_input;
  std::cout << "Would you like to play again? y/n" << std::endl;
  std::cin >> user_input;
  std::cout << "you entered: " << user_input << std::endl;
  if (user_input == "y") {
    board_->reset_board();
    return true;
  }
  return false;
}
