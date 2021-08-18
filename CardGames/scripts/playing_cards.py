"""
playing_cards module
Created on: Aug 04, 2021
Authors: Eric Victorson <vier0801@gmail.com>
Info: Module encompassing classes to represent playing cards and games
"""

import random

class Card:
    """
    A class to represent a standard playing deck.

    ...

    Attributes
    ----------
    POSSIBLE_VALUES : {str:int}
        class level (static attribute) dictionary of possible values
    POSSIBLE_SUITS : (str)
        class level (static attribute) tuple of possible suits
    POSSIBLE_RANKS : (str)
        class level (static attribute) tuple of possible ranks
    MAX_COUNT : int
        class level (static attribute) maximum number of object references
    count : int
        class level (static attribute) number of references
    suit : str
        suit of the card
    rank : str
        rank of the card
    value : int
        integer representation of rank

    """
    POSSIBLE_VALUES = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
                       'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':11,
                       'queen':12, 'king':13, 'ace':14}
    POSSIBLE_SUITS = ('hearts', 'diamonds', 'spades', 'clubs')
    POSSIBLE_RANKS = ('two', 'three', 'four', 'five', 'six', 'seven',
                      'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
    MAX_COUNT = 52
    count = 0

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank.lower()
        self.value = Card.POSSIBLE_VALUES[rank.lower()]
        Card.count += 1

    def __del__(self):
        Card.count -= 1

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit)

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

class Chips:
    """
    A class to represent a cache of poker chips

    ...

    Attributes
    ----------
    total : int
        number of chips available for betting
    bet : int
        number of chips currently wagered

    """
    def __init__(self, num_chips=100):
        self.total = num_chips
        self.bet = 0

    def win_bet(self):
        """ increment by bet amount when bet is won. """
        self.total += self.bet

    def lose_bet(self):
        """ decrement by bet amount when bet is lost. """
        self.total -= self.bet

class Deck:
    """
    A class to represent a standard 52 card playing deck.

    ...

    Attributes
    ----------
    all_cards : list[card]
        list of card objects

    """

    def __init__(self):
        self.all_cards = []
        self._create_deck()

    def __len__(self):
        return len(self.all_cards)

    def __getitem__(self, position):
        return self.all_cards[position]

    def _create_deck(self):
        """Creates the deck."""
        self.all_cards = [Card(suit, rank) for suit in Card.POSSIBLE_SUITS
                                           for rank in Card.POSSIBLE_RANKS]

    def shuffle(self):
        """Shuffles the deck. """
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        """
        Pops one card off the top of the all_cards list
        Returns card object.
        """
        return self.all_cards.pop()

class Hand:
    """
    A class to represent a hand in poker

    ...

    Attributes
    ----------
    cards : [card objects]
        list of cards in the players hand
    value : int
        cumulative value of the cards in the player's hand
    aces : int
        number of aces in the player's hand
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __len__(self):
        return len(self.cards)

    def add_card(self, card_in):
        """Add a card to the player's hand."""
        self.cards.append(card_in)
        self.value += card_in.value
        if card_in.rank == 'ace':
            self.aces += 1

    def adjust_for_ace(self):
        """Adjust the score for aces."""
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Player:
    """
    A class to represent a person playing a card game.

    ...

    Attributes
    ----------
    name : str
        player's name.
    all_cards : [card]
        list of cards in the players hand.
    """
    def __init__(self, name):
        self.name = name
        self.hand = []

    def remove_one_card(self):
        """ remove one card from the player """
        return self.hand.pop()

    def add_cards(self, new_cards):
        """ add cards to the player in the event they won """
        if isinstance(new_cards, list):
            # If a list of cards is passed, extend the current list
            self.hand.extend(new_cards)
        else:
            # If a single card is passed, just append it to the current list
            self.hand.append(new_cards)

    def __str__(self):
        return 'Player {} has {} cards'.format(self.name, len(self.hand))

if __name__ == '__main__':
    deck = Deck()
    print(deck.all_cards)

    print("\nShuffling deck.\n")
    deck.shuffle()
    print(deck.all_cards)

    print("\nnumber of cards created = {}".format(deck.all_cards[0].count))

    card = deck.deal_one_card()
    print("\nnumber of cards created = {}".format(deck.all_cards[0].count))
