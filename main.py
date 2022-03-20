import os
from time import sleep
from utils import input, clear

def newGame():
    pass

# Main menu
def main():
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
        clear()
        print("See you next time...")
        sleep(2)


# Initialization
if __name__ == "__main__":
    main()
    clear()
