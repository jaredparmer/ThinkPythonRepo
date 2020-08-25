""" exercise 18.3 of Downey, _Think Python_ 2nd ed.
"""

from Card import Card, Hand, Deck

class PokerHand(Hand):
    """ represents a poker hand.

    inherits from Hand, which inherits from Deck.

    instance attributes: cards, a list of Cards; and suits, a hist of suits
    """
    def __init__(self, label=''):
        self.label = str(label)
        self.cards = []
        self.suits = {}
        self.ranks = {}

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_four(self):
        """ checks for four of a kind. """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_three(self):
        """ checks for three of a kind. """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_two_pair(self):
        self.rank_hist()
        vals = list(self.ranks.values())
        vals.sort(reverse=True)
        if vals[0] >= 2 and vals[1] >= 2:
            return True
        return False
        

    def rank_hist(self):
        """ builds a histogram of ranks (card values, Ace to King) that appear
        in the hand, stores in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def suit_hist(self):
        """ builds a histogram of suits that appear in the hand, stores in
        attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1


def main():
    deck = Deck()
    deck.shuffle()
    for i in range(7):
        hand = PokerHand(f"hand {i + 1}")
        deck.draw(hand, 7)
        hand.sort()
        print(hand)
        print("has three of a kind: " + str(hand.has_three()))
        print('')


if __name__ == '__main__':
    main()
