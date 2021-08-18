/**
 *  tictactoe.h
 *
 *  Created on: Aug 17th, 2021
 *     Authors: Eric Victorson <vier0801@gmail.com>
 *        Info: class handling tictactoe gameplay
 *
 */

#ifndef TICTACTOE_H
#define TICTACTOE_H

#include "board.h"
#include <vector>
#include <iostream>
#include <string>
#include <memory>

class TicTacToe {
public:
  TicTacToe();
  TicTacToe(const TicTacToe&) = delete;
  ~TicTacToe();
  void run();

protected:
  void get_user_input();
  void toggle_player_num();
  int display_startup_message();
  bool check_for_replay();
  int get_and_validate_input();

  std::unique_ptr<Board> board_;
  int current_player_{0};
  const std::vector<std::string> PLAYER_SYMBOLS_{"X", "O"};
};

#endif //TICTACTOE_H
