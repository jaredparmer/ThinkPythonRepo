""" chapter 18 of Downey, _Think Python_ 2nd ed.
"""

import random


class Card:
    """ represents a playing card. """
    # class attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                  '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit=0, rank=2):
        # instance attributes
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        if other.suit < self.suit:
            return False
        return self.rank < other.rank
    

class Deck:
    """ represents a deck of playing cards. """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def __len__(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def draw(self, hand, n=1):
        for i in range(n):
            hand.add_card(self.pop_card())

    """ solves exercise 18.2 """
    def deal(self, n_hands, n_cards):
        if n_hands * n_cards > len(self):
            raise IndexError("not enough cards in deck!")
        res = []
        for i in range(n_hands):
            hand = Hand(f"hand {i + 1}")
            self.draw(hand, n_cards)
            res.append(hand)
        return res

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()


class Hand(Deck):
    """ represents a hand of playing cards. inherits from Deck. """
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return self.label + ':\n\t' + '\n\t'.join(res)

d = Deck()
d.shuffle()
hands = d.deal(5, 7)
for hand in hands:
    print(hand)
print("deck: " + str(d))
