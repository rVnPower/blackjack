import os
from time import sleep
from utils import input, clear, Game


def newGame():
    while True:
        game = Game()
        game.start()
        a = input("Do you want to play again?\n(y/n):").strip().lower()
        if a == "y":
            del game
        else:
            break

# Main menu
def main():
    clear()
    print(
    """
    Hello and welcome to Blackjack!

    1) New game
    2) Quit
    """
    )
    player_input = int(input())
    if player_input == 1:
        newGame()
    elif player_input == 2:
        return 


# Initialization
if __name__ == "__main__":
    main()
    clear()
    print("See you next time...")
    sleep(2)
    clear()
