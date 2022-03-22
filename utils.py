from random import shuffle
from time import sleep
import os 
# Assign `input` to `raw_input` because we are re-using its name 
raw_input = input

# Handle input
def input(placeholder: str = ""):
    while True:
        try:
            n = raw_input(placeholder)
            break
        except:
            print(
            """
            You are trying to exit the game...
            Press Ctrl-c again to exit
            Or wait 3 seconds to continue.
            """
            )
            sleep(3)
            print("Continuing...")
    return n

# Clear the terminal
def clear():
    os.system('clear')

# Game class
class Game:
    def __init__(self):
        self.playersDeck = []
        self.botsDeck = []

    def start(self):
        '''
        Start a new game
        '''
        ### Initialization
        # Creating decks
        clear()
        self.playersDeck, self.botsDeck = Deck(), Deck()
        self.cardsPile = Deck()
        self.cardsPile.fill()
        self.cardsPile.shuffle()

        # dealting first two cards
        for times in range(2):
            self.playersDeck.deal(self.cardsPile)
            self.botsDeck.deal(self.cardsPile)
        self.playersDeck.calculate()
        self.botsDeck.calculate()

        print(f"You have {self.playersDeck.points}")
        print(" ".join(self.playersDeck.getRawCards()))
        if self.playersDeck.won:
            print("You got a blackjack!")

        while not (self.playersDeck.standed or self.playersDeck.busted or self.playersDeck.won):
            self.handlePlayer()

        print("_______________________________________________________________________________")

        self.handleBot()
        print(self.checkWon())

    def handlePlayer(self):
        inputs = input("(deal/stand): ").strip().lower()

        if inputs in ["deal", "hit", "1"]:
            self.playersDeck.deal(self.cardsPile)
            self.playersDeck.calculate()
        elif inputs in ["stand", "2"]:
            self.playersDeck.stand()

        print(f"You now have {self.playersDeck.points}")
        print(" ".join(self.playersDeck.getRawCards()))

        if self.playersDeck.checkIfBusted():
            print("You busted!")
            

    def handleBot(self):
        deck = self.botsDeck
        print(f"Bot has {deck.points}")
        print(" ".join(deck.getRawCards()))
        if deck.won:
            print("Bot got a blackjack!")

        if self.playersDeck.busted:
            deck.stand()
            print("Bot standed!")

        while not (deck.standed or deck.busted or deck.won):

            if deck.points < 17:
                deck.deal(self.cardsPile)
                self.botsDeck.calculate()
                print(f"Bot has {deck.points}")
                print(" ".join(deck.getRawCards()))
            else:
                deck.stand()

            if deck.checkIfBusted():
                print("Bot busted!")

        self.botsDeck = deck

    def checkWon(self):
        '''
        Check who won
        '''
        bot = self.botsDeck
        player = self.playersDeck
        if bot.points == player.points or (bot.busted and player.busted) or (bot.won and player.won):
            return "It's a tie!"
        elif (player.points > bot.points or bot.busted or player.won) and not player.busted:
            return "Player won!"
        elif (player.points < bot.points or player.busted or bot.won) and not bot.busted:
            return "Bot won!"

# Card class represent a card
class Card:
    def __init__(self, suit, index, points):
        self.suit = suit
        self.index = index
        self.points = points

    def getSuit(self):
        return self.suit

    def getPoints(self):
        return self.points

    def getRaw(self):
        return f"{self.index}{self.suit}"

# Deck class represent a deck
class Deck:
    def __init__(self):
        self.cards = []
        self.standed = False
        self.busted = False
        self.won = False
        self.points = 0

    def fill(self):
        '''
        Fill the deck with cards
        '''
        if len(self.cards) > 0:
            return

        for number in range(1, 13+1):
            card_index = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][number-1]
            card_points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10][number-1]
            # Aces got 11 points by default, may change in `calculate` function below.

            for suit in ['♠', '♦', '♣', '♥']:
                card = Card(suit, card_index, card_points)
                self.cards.append(card)

    def pop(self):
        '''
        Remove and return the last element in the deck
        '''
        return self.cards.pop()

    def getRawCards(self):
        '''
        Return list of raw cards which contains suit and its values
        '''
        lst = []
        for card in self.cards:
            lst.append(card.getRaw())
        return lst


    def checkIfBusted(self):
        '''
        Check if this deck busted or not
        '''
        if self.points > 21:
            self.busted = True

        return self.busted

    def checkIfBlackjack(self):
        if 2 > self.cards.count("A") > 0 and (
            self.cards.count("10") > 0
            or self.cards.count("J") > 0
            or self.cards.count("Q") > 0
            or self.cards.count("K") > 0
        ):
            self.won = True


    def deal(self, pile):
        '''
        Deal a card
        '''
        popped_card = pile.pop()
        self.cards.append(popped_card)

    def stand(self):
        '''
        Stand
        '''
        self.standed = True

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

    def calculate(self):
        aces = []
        calculated_points = 0
        for card in self.cards:
            if card.index == "A" and card.getPoints() == 11:
                aces.append(card)
                continue
            calculated_points += card.getPoints()

        for ace in aces:
            if 11 + calculated_points > 21:
                ace.points = 1
            calculated_points += ace.points

        self.checkIfBlackjack()

        self.points = calculated_points

    def reset(self):
        '''
        Return all values to default
        '''
        self.cards.flush()
        self.points = 0
        self.standed = False
        self.busted = False
        self.won = False

    def debug(self):
        '''
        Print all class properties (not meant to be user-friendly)
        '''
        print(self.cards)
        print(self.filled)
        print(self.points)
