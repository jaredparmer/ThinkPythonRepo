""" exercise 18.3 of Downey, _Think Python_ 2nd ed.
"""

from Card import Card, Hand, Deck

class PokerHand(Hand):
    """ represents a poker hand.

    inherits from Hand, which inherits from Deck.

    instance attributes: cards, a list of Cards; and suits, a hist of suits
    """
    all_labels = [' has a straight flush', ' has four of a kind',
                  ' has a full house', ' has a flush', ' has a straight',
                  ' has three of a kind', ' has two pairs', ' has one pair',
                  ' has a high card']
    
    def __init__(self, label=''):
        self.label = str(label)
        self.cards = []
        self.suits = {}
        self.ranks = {}
        self.sets = []


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
        self.setup()

        if self.has_straight_flush():
            self.label += ' has a straight flush'
        elif self.has_four():
            self.label += ' has four of a kind'
        elif self.has_full_house():
            self.label += ' has a full house'
        elif self.has_flush():
            self.label += ' has a flush'
        elif self.has_straight():
            self.label += ' has a straight'
        elif self.has_three():
            self.label += ' has three of a kind'
        elif self.has_two_pair():
            self.label += ' has two pairs'
        elif self.has_pair():
            self.label += ' has one pair'
        else:
            self.label += ' has a high card'


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


    def has_straight(self, n=5):
        if len(self.cards) < n:
            # special case: PokerHand has insufficient cards for a straight
            return False
        
        ranks = list(self.ranks.keys())
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

        """ special case: 10-J-Q-K-A straights, which is special because Aces
        are coded as rank 1, but should also be considered to have highest
        rank. """
        if {1, 10, 11, 12, 13} <= set(ranks):
            return True
        
        return False


    def has_straight_flush(self, n=5):
        # step one: partition PokerHand by suit
        clubs = PokerHand()
        diamonds = PokerHand()
        hearts = PokerHand()
        spades = PokerHand()

        for card in self.cards:
            if card.suit == 0:
                clubs.add_card(card)
            elif card.suit == 1:
                diamonds.add_card(card)
            elif card.suit == 2:
                hearts.add_card(card)
            else:
                spades.add_card(card)

          # need rank histogram for has_straight(), so
        clubs.setup()
        diamonds.setup()
        hearts.setup()
        spades.setup()

        # step two: see if any partitioned PokerHand has a straight
        return (clubs.has_straight()
                or diamonds.has_straight()
                or hearts.has_straight()
                or spades.has_straight())
        
    def has_three(self):
        """ checks for three of a kind. """
        return self.check_sets(3)


    def has_two_pair(self):
        return self.check_sets(2, 2)


    def setup(self):
        """ builds histogram of ranks, histogram of suits, and sorted
        list of rank sets in hand. """
        self.sort_by_rank()
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
            
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

    def sort_by_rank(self):
        """ Sorts Cards by rank. Use self.sort() to sort Cards by suit. """
        self.cards = sorted(self.cards, key=lambda card: card.rank)


def main():
    n = 100000
    freqs = {}

    for i in range(n):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.draw(hand, 5)
        hand.classify()
        freqs[hand.label] = freqs.get(hand.label, 0) + 1

    print("Estimated probabilities:")
    for key in PokerHand.all_labels:
        print(f"{key} \t\t {(freqs.get(key, 0) / n):.10f}")


if __name__ == '__main__':
    main()
