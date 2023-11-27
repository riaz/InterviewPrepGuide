import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits  = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [ Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    

if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()

    print(choice(deck))

    # adhering to python data model hence directly supports slicing
    print(deck[:3])
    #obj = deck[int(random.random()*len(deck))]

    # implementing getitem also makes in iterable

    for item in deck:
        print(item)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spade_high(card):
        rank_values = FrenchDeck.ranks.index(card.rank)
        return rank_values * suit_values[card.suit] * len(suit_values)
    
    for card in sorted(deck, key=spade_high):
        print(card)


