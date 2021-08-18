""" tic tac toe """
from typing import Tuple, List

class TicTacToe:
    """ Class representing a game of tic tac toe  of n dimensionality"""
    PLAYER_SYMBOLS = ['X', 'O']
    EMPTY_SPACE = ' '

    def __init__(self, size: int):
        self.size = int(size)
        self.board = self.generate_new_board(self.size)
        self.current_player = 0

    def generate_new_board(self, size: int) -> List[List]:
        """ Create a new empty board and return it. """
        board = [[self.EMPTY_SPACE for i in range(size)] for j in range(size)]
        return board

    def display_board(self):
        """ Display the board. """
        print('\n')
        for row_idx, row in enumerate(self.board):
            row_string = ''
            for col_idx, col in enumerate(row):
                if col_idx < len(row)-1:
                    row_string += col + ' | '
                else:
                    row_string += col

            print(row_string)

            horizontal = '-' * len(row_string)
            if row_idx < len(row) - 1:
                print(horizontal)
        print('\n')

    def reset_board(self):
        """ Reset the board. """
        self.board = self.generate_new_board(self.size)

    def check_for_end_condition(self) -> bool:
        """ Check if someone has won or a stalemate has occurred. """
        curr_player = not self.current_player
        if self.check_for_vertical_win():
            print(f'\n** User {int(curr_player) + 1} won vertically!**')
            return True
        elif self.check_for_horizontal_win():
            print(f'\n** User {int(curr_player) + 1} won horizontally!**')
            return True
        elif self.check_for_negative_diagonal_win():
            print(f'\n** User {int(curr_player) + 1} won diagonally!**')
            return True
        elif self.check_for_positive_diagonal_win():
            print(f'\n** User {int(curr_player) + 1} won diagonally!**')
            return True
        elif self.check_for_stalemate():
            return True
        return False

    def check_for_vertical_win(self) -> bool:
        """ Check if a user has won vertically. """
        for col_idx, _ in enumerate(self.board):
            column = []
            for row in self.board:
                column.append(row[col_idx])
            if self.check_all_elements_same(column):
                return True
        return False

    def check_for_horizontal_win(self) -> bool:
        """ Check if a user has won horizontally. """
        for row in self.board:
            if self.check_all_elements_same(row):
                return True
        return False

    def check_all_elements_same(self, list_in: List) -> bool:
        """ Check if all elements in a list are the same. """
        if list_in.count(list_in[0]) == len(list_in) and list_in[0] != self.EMPTY_SPACE:
            return True
        return False

    def check_for_positive_diagonal_win(self) -> bool:
        """ Check if a user has won diagonally positive slope. """
        diagonal = []
        col_idx = self.size - 1
        for row in self.board:
            diagonal.append(row[col_idx])
            col_idx -= 1
        if self.check_all_elements_same(diagonal):
            return True
        return False

    def check_for_negative_diagonal_win(self) -> bool:
        """ Check if a user has won diagonally with negative slope. """
        diagonal = []
        col_idx = 0
        for row in self.board:
            diagonal.append(row[col_idx])
            col_idx += 1
        if self.check_all_elements_same(diagonal):
            return True
        return False

    def check_for_stalemate(self) -> bool:
        """ Check if a stalemate has occurred. """
        num_empty_spaces = 0
        for row_idx, _ in enumerate(self.board):
            for col_idx, _ in enumerate(self.board):
                if self.board[row_idx][col_idx] == self.EMPTY_SPACE:
                    num_empty_spaces += 1

        if num_empty_spaces == 0:
            print('\n --- Stalemate! ---')
            return True
        return False

    def get_user_input(self):
        """ Get user input. """
        print(f'Player {self.current_player + 1}: ')

        space_empty = False
        while not space_empty:
            row_valid = False
            col_valid = False
            while not row_valid:
                row_input = input('Enter the row you would like to place a marker in: ')
                row_valid = self.validate_user_input(row_input)
            while not col_valid:
                col_input = input('Enter the column you would like to place a marker in: ')
                col_valid = self.validate_user_input(col_input)
            row_input = int(row_input)
            col_input = int(col_input)
            space_empty = self.validate_space_empty((row_input, col_input))

        self.add_marker_to_board((int(row_input), int(col_input)))

    def validate_space_empty(self, position: Tuple) -> bool:
        """ Validate that the space on the board is empty. """
        if self.board[position[0]][position[1]] == self.EMPTY_SPACE:
            return True
        print('Sorry, that space is taken, please enter an empty position.\n')
        return False

    def add_marker_to_board(self, position: Tuple):
        """ Add the user input to the board. """
        self.board[position[0]][position[1]] = self.PLAYER_SYMBOLS[self.current_player]

    def validate_user_input(self, user_input: int) -> bool:
        """ Check that the user input is valid. """
        if not user_input.isdigit():
            print('Please enter an integer input!')
            return False
        elif int(user_input) < 0 or int(user_input) > self.size:
            print(f'Please enter a number greater than 0 and less than {self.size}.')
            return False
        return True

    def toggle_player_num(self):
        """ Toggle to the other player. """
        self.current_player = not self.current_player

    def display_startup_message(self):
        """ Display the welcome prompt. """
        print('Welcome to Tic Tac Toe!')

    def check_for_replay(self):
        """ Check if a user would like to play another game. """
        user_input = input('Would you like to play again? y/n \n')
        if user_input.lower() == 'y':
            return True
        return False

    def run(self):
        """ Play the game. """
        self.display_startup_message()
        replay = True
        while replay:
            self.reset_board()
            self.display_board()

            while not self.check_for_end_condition():
                self.get_user_input()
                self.toggle_player_num()
                self.display_board()

            replay = self.check_for_replay()


if __name__ == '__main__':
    board_size = input('Input the size of the tic tac toe board: ')
    ttt = TicTacToe(board_size)
    ttt.run()
