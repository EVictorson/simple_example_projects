#include <gtest/gtest.h>
#include <memory>
#include <iostream>
#include "board.h"

using namespace testing;

class BoardTestFixture : public Test {
public:
  int board_size{3};
  const std::string EMPTY_SPACE{" "};
  std::unique_ptr<Board> board;

  void SetUp() override {
    board = std::make_unique<Board>(board_size);
  }

  void TearDown() override {
  }

};

TEST_F(BoardTestFixture, EmptyBoardTest) {
  int board_size = board->get_size();
  bool all_cells_empty = true;
  //TODO: break out into helper function, code duplication
  for (int row_idx = 0; row_idx < board_size; row_idx++) {
    for (int col_idx = 0; col_idx < board_size; col_idx++) {
      if (board->get_element(row_idx, col_idx) != EMPTY_SPACE) {
        all_cells_empty = false;
      }
    }
  }

  EXPECT_EQ(all_cells_empty, true);
}

TEST_F(BoardTestFixture, AddMarkerTestX) {
  int row{0};
  int col{0};
  std::string marker = "X";

  board->add_marker(row, col, marker);
  std::string element = board->get_element(row, col);

  EXPECT_EQ(marker, element);
}


TEST_F(BoardTestFixture, ResetBoardTest) {
  int row{0};
  int col{0};
  std::string marker = "X";
  board->add_marker(row, col, marker);

  board->reset_board();

  //TODO: break out into helper function, code duplication
  int board_size = board->get_size();
  bool all_cells_empty = true;
  for (int row_idx = 0; row_idx < board_size; row_idx++) {
    for (int col_idx = 0; col_idx < board_size; col_idx++) {
      if (board->get_element(row_idx, col_idx) != EMPTY_SPACE) {
        all_cells_empty = false;
      }
    }
  }

  EXPECT_EQ(all_cells_empty, true);
}

TEST_F(BoardTestFixture, HorizontalWinTest) {
  std::string marker = "X";
  int board_size = board->get_size();
  int row{0};
  bool end_condition;

  for (int col = 0; col < board_size; col++) {
    board->add_marker(row, col, marker);
    end_condition = board->check_for_end_condition();
    if (col < board_size - 1) {
      EXPECT_EQ(end_condition, false);
    }
  }

  end_condition = board->check_for_end_condition();
  EXPECT_EQ(end_condition, true);
}

TEST_F(BoardTestFixture, VerticalWinTest) {
  std::string marker = "X";
  int board_size = board->get_size();
  int col{0};
  bool end_condition;

  for (int row = 0; row < board_size; row++) {
    board->add_marker(row, col, marker);
    end_condition = board->check_for_end_condition();
    if (row < board_size - 1) {
      EXPECT_EQ(end_condition, false);
    }
  }

  end_condition = board->check_for_end_condition();
  EXPECT_EQ(end_condition, true);
}


int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
