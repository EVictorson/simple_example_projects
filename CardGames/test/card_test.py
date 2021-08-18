#!/usr/bin/env python3

import unittest
import sys
sys.path.append('../')
from playing_cards import Card

class TestCard(unittest.TestCase):
    POSSIBLE_VALUES = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
                       'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':11,
                       'queen':12, 'king':13, 'ace':14}
    POSSIBLE_SUITS = ('hearts', 'diamonds', 'spades', 'clubs')
    POSSIBLE_RANKS = ('two', 'three', 'four', 'five', 'six', 'seven',
                      'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
    MAX_COUNT = 52
    my_card = Card(Card.POSSIBLE_SUITS[0], Card.POSSIBLE_RANKS[0])

    def setUp(self):
        pass

    def test_possible_values(self):
        self.assertEqual(self.my_card.POSSIBLE_VALUES, self.POSSIBLE_VALUES)

    def test_possible_suits(self):
        self.assertEqual(self.my_card.POSSIBLE_SUITS, self.POSSIBLE_SUITS)

    def test_possible_ranks(self):
        self.assertEqual(self.my_card.POSSIBLE_RANKS, self.POSSIBLE_RANKS)

    def test_first_card(self):
        self.assertEqual(self.my_card, Card('hearts','two'))


if __name__ == '__main__':

    unittest.main()
