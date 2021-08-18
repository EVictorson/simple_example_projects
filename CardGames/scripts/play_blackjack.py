"""
play_blackjack.py
Created on: Aug 04, 2021
Authors: Eric Victorson <vier0801.gmailcom>
Info: class to play the cardgame blackjack
"""

from playing_cards import *

class PlayBlackJack:
    """
    A class to represent the modified play of a game of blackjack

    ...

    Attributes
    ----------
    player_chips : playing_cards.Chips object
        player's available cache of betting chips
    deck : playing_cards.Deck object
        object representing 52 card deck
    player_hand : playing_cards.Hand object
        object representing the hand of the user
    dealer_hand : playing_cards.Hand object
        object representing the hand of the dealer
    playing : bool
        boolean indicating whether or not play should continue
    """

    def __init__(self):
        self.player_chips = Chips()
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.playing = True

    def take_bet(self, chips):
        """ take the number of chips being bet by the user. """
        while True:
            try:
                chips.bet = int(input('How many chips would you like to bet?\n'))
            except ValueError:
                print('Please enter an integer number of chips to bet.')
            else:
                if chips.bet > chips.total:
                    print('Your bet cannot exceed your current balance of {}'.format(chips.total))
                else:
                    break

    def hit(self, deck, hand):
        """ perform a hit (draw another card). """
        hand.add_card(deck.deal_one_card())
        hand.adjust_for_ace()
        print(hand.cards)

    def hit_or_stand(self, deck, hand):
        """ ask user if they would like to hit or stand. """
        while True:
            user_in = input('Would you like to hit or stand? Enter "h" or "s"\n')

            if user_in[0].lower() == 'h':
                self.hit(deck, hand)
            elif user_in[0].lower() == 's':
                print('Player stands.  Dealer is playing.')
                self.playing = False
            else:
                print('Sorry, please try again.')
                continue
            break

    def show_some_cards(self, dealer, player):
        """ show user cards but only one dealer card. """
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='\n ')

    def show_all_cards(self, dealer, player):
        """ show all of everyone's cards. """
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =", player.value)

    def player_busts(self, player, dealer, chips):
        """ condition if player goes over 21. """
        print("Player busts!")
        chips.lose_bet()

    def player_wins(self, player, dealer, chips):
        """ condition if player wins. """
        print("Player wins!")
        chips.win_bet()

    def dealer_busts(self, player, dealer, chips):
        """ condition if dealer goes over 21. """
        print("Dealer busts!")
        chips.win_bet()

    def dealer_wins(self, player, dealer, chips):
        """ condition if dealer wins. """
        print("Dealer wins!")
        chips.lose_bet()

    def push(self, player, dealer):
        """ condition if it's a draw. """
        print("Dealer and Player tie! It's a push.")

    def print_opening_statement(self):
        """ print the welcome statement."""
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

    def deal_n_cards(self, n):
        """ deal n number of cards. """
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        for _ in range(n):
            self.player_hand.add_card(self.deck.deal_one_card())
            self.dealer_hand.add_card(self.deck.deal_one_card())


    def play_dealers_hand(self):
        """ continue playing dealer's hand. """
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if self.player_hand.value <= 21:

            while self.dealer_hand.value < 17:
                self.hit(self.deck, self.dealer_hand)

            self.show_all_cards(self.dealer_hand, self.player_hand)

            # Run different winning scenarios
            if self.dealer_hand.value > 21:
                self.dealer_busts(self.player_hand, self.dealer_hand, self.player_chips)

            elif self.dealer_hand.value > self.player_hand.value:
                self.dealer_wins(self.player_hand, self.dealer_hand, self.player_chips)

            elif self.dealer_hand.value < self.player_hand.value:
                self.player_wins(self.player_hand, self.dealer_hand, self.player_chips)

            else:
                self.push(self.player_hand, self.dealer_hand)

    def continue_playing(self):
        """ check if user wants to continue playing. """
        # Inform Player of their chips total
        print("\nPlayer's winnings stand at", self.player_chips.total)

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            self.playing = True
            return True
        else:
            print("Thanks for playing!")
            return False

    def play_game(self):
        """ play the game of blackjack. """
        while True:

            self.deal_n_cards(2)
            self.take_bet(self.player_chips)
            self.show_some_cards(self.dealer_hand, self.player_hand)

            while self.playing:
                self.hit_or_stand(self.deck, self.player_hand)
                self.show_some_cards(self.dealer_hand, self.player_hand)

                if self.player_hand.value > 21:
                    self.player_busts(self.player_hand, self.dealer_hand, self.player_chips)
                    break

            self.play_dealers_hand()
            if self.continue_playing():
                continue
            else:
                break

if __name__ == '__main__':
    pbj = PlayBlackJack()
    pbj.play_game()
