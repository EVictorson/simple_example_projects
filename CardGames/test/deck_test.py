#!/usr/bin/env python3

import unittest
import copy
import sys
sys.path.append('../')
from playing_cards import Deck

class TestDeck(unittest.TestCase):

    deck = Deck()

    def setUp(self):
        self.deck = Deck()

    def test_correct_number_of_cards(self):
        self.assertEqual(len(self.deck.all_cards), 52)

    def test_pop_removes_card(self):
        self.deck.deal_one_card()
        self.assertEqual(len(self.deck.all_cards), 51)

    def test_pop_returns_card(self):
        card1 = self.deck.all_cards[-1]
        card2 = self.deck.deal_one_card()
        self.assertEqual(card1, card2)

    def test_shuffle(self):
        all_cards1 = copy.deepcopy(self.deck.all_cards)
        self.deck.shuffle()
        all_cards2 = self.deck.all_cards

        if all_cards1 == all_cards2:
            decks_are_equal = True
        else:
            decks_are_equal = False
        self.assertEqual(decks_are_equal, False)


if __name__ == '__main__':
    unittest.main()
