"""
play_war.py
Created on: Aug 04, 2021
Authors: Eric Victorson <vier0801.gmailcom>
Info: class to play the cardgame war
"""

from playing_cards import *

class PlayWar:
    """
    A class to represent the play of a game of war

    ...

    Attributes
    ----------
    NUM_DRAWN_CARDS : int
        number of cards to be drawn in the case of war
    player1 : player object
        object representing player one
    player2 : player object
        object representing player two
    player1_played_cards : [card]
        list of card objects played in this turn by player1
    player2_played_cards : [card]
        list of card objects played in this turn by player2
    new_deck : deck object
        current deck of cards
    round_number : int
        number of rounds elapsed in the game
    game_on : bool
        boolean indicating if the game is currently being played
    at_war : bool
        boolean indicating if war is occurring
    """
    NUM_DRAWN_CARDS = 3

    def __init__(self):
        self.player1 = Player("one")
        self.player2 = Player("Two")
        self.player1_played_cards = []
        self.player2_played_cards = []
        self.new_deck = Deck()
        self.new_deck.shuffle()
        self.deal_cards()
        self.round_number = 0
        self.game_on = True
        self.at_war = True

    #TODO: refactor this to be composed of multiple function calls
    def play(self):
        """ Play the game of war. """
        while self.game_on:
            self.round_number += 1
            print(f"Round {self.round_number}")

            if self.check_win_condition():
                break
            self.start_next_round()

            while self.at_war:
                # Use last card to always be comparing last card when war occurs
                if self.player1_played_cards[-1].value > self.player2_played_cards[-1].value:
                    self.player1.add_cards(self.player1_played_cards)
                    self.player1.add_cards(self.player2_played_cards)
                    print("player 1 wins this round")
                    self.at_war = False

                elif self.player2_played_cards[-1].value > self.player1_played_cards[-1].value:
                    self.player2.add_cards(self.player1_played_cards)
                    self.player2.add_cards(self.player2_played_cards)
                    print("player 2 wins this round")
                    self.at_war = False

                else:
                    print('WAR!')

                    if len(self.player1.hand) < self.NUM_DRAWN_CARDS:
                        print("Player one unable to declare war")
                        print("Player Two Wins!")
                        self.game_on = False
                        break

                    elif len(self.player2.hand) < self.NUM_DRAWN_CARDS:
                        print("Player two unable to declare war")
                        print("Player One Wins!")
                        self.game_on = False
                        break

                    else:
                        for _ in range(self.NUM_DRAWN_CARDS):
                            self.player1_played_cards.append(self.player1.remove_one_card())
                            self.player2_played_cards.append(self.player2.remove_one_card())

    def deal_cards(self):
        """ split deck and deal cards to players """
        for _ in range(int(Card.MAX_COUNT/2)):
            self.player1.add_cards(self.new_deck.deal_one_card())
            self.player2.add_cards(self.new_deck.deal_one_card())

    def check_win_condition(self):
        """ check if either player has won the game. """
        if self.check_player_one_game_win() or self.check_player_two_game_win():
            return True

        return False

    def check_player_one_game_win(self):
        """ check if player one has won the game. """
        if len(self.player2.hand) == 0:
            print("Player two is out of cards!  Player one wins!")
            self.game_on = False
            return True
        return False

    def check_player_two_game_win(self):
        """ check if player two has won the game. """
        if len(self.player1.hand) == 0:
            print("Player one is out of cards!  Player two wins!")
            self.game_on = False
            return True
        return False

    def start_next_round(self):
        """ start the next round of the game. """
        self.at_war = True
        self.player1_played_cards = []
        self.player1_played_cards.append(self.player1.remove_one_card())

        self.player2_played_cards = []
        self.player2_played_cards.append(self.player2.remove_one_card())

if __name__ == '__main__':
    pw = PlayWar()
    pw.play()
