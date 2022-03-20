from random import shuffle

# Game class
class Game:
    def __init__(self):
        self.cardsPile = []
        self.playersDeck = []
        self.botsDeck = []

    def start(self):
        '''
        Start a new game
        '''
        ### Initialization
        # Creating decks
        self.playersDeck, self.botsDeck = Deck(), Deck()
        self.cardsPile = Deck()
        self.cardsPile.fill()
        self.cardsPile.shuffle()

        # Hitting first two cards
        for times in range(2):
            self.playersDeck.hit(self.cardsPile)
            self.botsDeck.hit(self.cardsPile)

        for i in self.playersDeck.cards:
            print(i.getSuit(), end="")

        for i in self.botsDeck.cards:
            print(i.getSuit(), end="")

# Card class represent a card
class Card:
    def __init__(self, suit, points):
        self.suit = suit
        self.points = points

    def getSuit(self):
        return self.suit

# Deck class represent a deck
class Deck:
    def __init__(self):
        self.cards = []
        self.filled = False
        self.points = 0

    def fill(self):
        '''
        Fill the deck with cards
        '''
        if len(self.cards) > 0:
            return

        for number in range(1, 13+1):
            card_index = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][number-1]
            card_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10][number-1]
            for suit in ['♠', '♦', '♣', '♥']:
                card = Card(f"{card_index}{suit}", card_points)
                self.cards.append(card)
        self.filled = True

    def pop(self):
        '''
        Remove and return the last element in the deck
        '''
        return self.cards.pop()

    def hit(self, pile):
        '''
        Draw a card
        '''
        self.cards.append(pile.pop())

    def flush(self):
        '''
        Remove all cards in deck
        '''
        self.cards = []
        self.filled = False

    def shuffle(self):
        '''
        Shuffle the deck randomly
        '''
        shuffle(self.cards)

    def refresh(self):
        '''
        Refresh all class properties
        '''
        pass

    def debug(self):
        '''
        Print all class properties (not meant to be user-friendly)
        '''
        print(self.cards)
        print(self.filled)
        print(self.points)
