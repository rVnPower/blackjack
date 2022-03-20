import os
from time import sleep

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

def clear():
    os.system('clear')

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
