'''
Problem 54 - Poker Hands

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
'''

from enum import IntEnum
from itertools import groupby
from lib.config import assets_path
from lib.helpers.runtime import print_answer_and_elapsed_time


class Card:
    def __init__(self, card_string):
        self.value = card_string[0]
        self.suit = card_string[1]

    def __repr__(self):
        return 'Card(value=%r, suit=%r)' % (self.value, self.suit)

    def __sub__(self, other):
        return self.rank() - other.rank()

    def __lt__(self, other):
        return self.rank() < other.rank()

    def rank(self):
        try:
            return int(self.value)
        except:
            if self.value == 'T':
                return 10
            if self.value == 'J':
                return 11
            if self.value == 'Q':
                return 12
            if self.value == 'K':
                return 13
            if self.value == 'A':
                return 14


class Hands(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class Hand:
    def __init__(self, cards):
        self.cards = sorted(
            [Card(card) for card in cards][:5],
            key=lambda card: card.rank(),
            reverse=True,
        )

    def __repr__(self):
        return 'Hand(cards=%r)' % (self.cards)

    def __lt__(self, other):
        self_hand = self.rank()
        other_hand = other.rank()

        if self_hand[0] < other_hand[0]:
            return True

        if other_hand[0] < self_hand[0]:
            return False

        for (self_card, other_card) in zip(self_hand[1], other_hand[1]):
            if self_card < other_card:
                return True

            if other_card < self_card:
                return False

        return False

    def is_wheel(self):
        return self.cards[0].value == 'A' \
            and self.cards[1].value == '5' \
            and self.cards[2].value == '4' \
            and self.cards[3].value == '3' \
            and self.cards[4].value == '2'

    def rank(self):
        sets = sorted(
            [(rank, len(list(grouper)))
             for (rank, grouper)
             in groupby(self.cards, key=lambda card: card.rank())],
            key=lambda set: (set[1], set[0]),
            reverse=True,
        )
        tie_breakers = [value for (value, _) in sets]
        sets_length = len(sets)

        if sets_length == 4:
            return (Hands.ONE_PAIR, tie_breakers)

        if sets_length == 3:
            if sets[0][1] == 2:
                return (Hands.TWO_PAIR, tie_breakers)

            if sets[0][1] == 3:
                return (Hands.THREE_OF_A_KIND, tie_breakers)

        if sets_length == 2:
            if sets[0][1] == 3:
                return (Hands.FULL_HOUSE, tie_breakers)

            if sets[0][1] == 4:
                return (Hands.FOUR_OF_A_KIND, tie_breakers)

        straight = self.is_wheel() or \
            all([i == 0 or self.cards[i - 1] - card == 1
                 for (i, card) in enumerate(self.cards)])
        flush = len(list(groupby(self.cards, key=lambda card: card.suit))) == 1

        if flush and straight:
            return (Hands.STRAIGHT_FLUSH, tie_breakers)

        if flush and not straight:
            return (Hands.FLUSH, tie_breakers)

        if straight:
            return (Hands.STRAIGHT, tie_breakers)

        return (Hands.HIGH_CARD, tie_breakers)


def answer():
    with open('%s/problem54/poker.txt' % assets_path) as file:
        def parse(line):
            cards = line.split(' ')
            return (Hand(cards[:5]), Hand(cards[5:]))

        return sum([1
                    for (hand1, hand2) in [parse(line) for line in file]
                    if hand1 > hand2])

if __name__ == '__main__':
        print_answer_and_elapsed_time(answer)
