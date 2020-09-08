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


    def check_sets(self, *t):
        """ t is a list of ints, with number of elements being the number of
        sets to check for, and the elements being the length within each set to
        check for. t should be sorted from longest set to shortest set.
        For example, checking for two pairs is t = [2, 2], checking for a full
        house is t = [3, 2], and checking for four of a kind is t = [4]. """
        for need, have in zip(t, self.sets):
            if need > have:
                return False
        return True

        
    def classify(self):
        """ identifies best hand (pair, two pair, etc.) in poker hand. """

        """ set up: build histogram of ranks, histogram of suits, and sorted
        list of rank sets in hand. """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
            
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

        """ identification phase. """
        # TBD


    def has_flush(self):
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


    def has_four(self):
        """ checks for four of a kind. """
        return self.check_sets(4)


    def has_full_house(self):
        return self.check_sets(3, 2)


    def has_pair(self):
        return self.check_sets(2)


    def has_straight(self):
        ranks = list(self.ranks.keys())
        ranks.sort()
        prev_rank = ranks[0] - 1
        # length of run found so far; resets to 1 when run is broken
        count = 0
        for i in range(len(ranks)):
            if ranks[i] - prev_rank == 1:
                count += 1
                if count == n:
                    return True
            else:
                count = 1

            prev_rank = ranks[i]

        """ special case: 10-J-Q-K-A type runs, where Aces, coded as rank 1,
        also should be considered to have highest rank. """
        if count == n - 1 and 1 in ranks:
            return True
        
        return False

        
    def has_three(self):
        """ checks for three of a kind. """
        return self.check_sets(3)


    def has_two_pair(self):
        return self.check_sets(2, 2)


def main():
    deck = Deck()
    deck.shuffle()
    for i in range(7):
        hand = PokerHand(f"hand {i + 1}")
        deck.draw(hand, 7)   
        hand.classify()
        print(hand)
        if hand.has_pair():
            print("has two of a kind")
        if hand.has_two_pair():
            print("has two pair")
        if hand.has_three():
            print("has three of a kind")
        if hand.has_straight():
            print("has straight")
        if hand.has_flush():
            print("has flush")
        if hand.has_full_house():
            print("has full house")
        if hand.has_four():
            print("has four of a kind")
        print('')


if __name__ == '__main__':
    main()
