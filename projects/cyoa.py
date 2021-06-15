"""Roulette Simulator."""

import time
import random
from random import randint

__author__: str
__author__ = "730384155"


# Globals
EMOJI: str = "\U000F190D"
zero: int = 0
one: int = 1
k: int = 2
m: int = 1
player: str = ""
points: int
color_generator: list[int] = [0, 1]
number_range: list[int] = list(range(0, 37))
COLOR: int = random.choice(color_generator)
NUMBER: int = random.choice(number_range)
T: bool = True
F: bool = False


def main() -> None:
    """Entrypoint of the program."""
    global points
    global m
    if m == 1:
        points = 50
        m += 1
    else:
        points = points
    while True:
        options: str = input("Would you like to end your experience at The Old Well Casino?[Yes/No]: ")
        if options == "No":
            side_or_main: str = input("Would you like to play the main game(Roulette) or side game?[Main/Side]: ")
            if side_or_main == "Main":
                greet()
                time.sleep(k + 1)
                points = roulette_round(m, points)
                what_now()
            elif side_or_main == "Side":
                """Entrypoint of side_game."""
                side_game()
            else:
                print("Try your syntax again, this program is case sensitive!")
                main()
        elif options == "Yes":
            print("I hope you enjoyed playing with us today at the Old Well Casino!")
            print(f"Ending Bank Balance: {points}")
        return None
    

def greet() -> None:
    """Greeting/Welcome Message."""
    global points
    player_input: str = input("Type \"Start\" and then press return to begin: ")
    if player_input == "Start" or "start":
        global player
        print(f"Welcome to the Old Well Casino!{EMOJI}")
        time.sleep(k)
        print("Today we will be playing Roulette.")
        print("Esentially, you will start off with a set amount of money.")
        print("When prompted, you will place a bet of any amount your bank account")
        print("will allow for on a single number (between 1 - 36).") 
        print("If one of your guessed number/numbers matches up with the winning number") 
        print("revealed by the dealer, then your money goes up!")
        print("Let's see if you know when to walk away from the table.")
        time.sleep(k)
        print(f"You have ${points}, so make sure your bet is equal to or below that value.")
        name_input: str = input("Enter your player name: ")
        player = name_input
    else:
        print("Nice spelling, try again.")
        time.sleep(k + 1)
        greet()


def roulette_round(round_num: int, current_points: int) -> int:
    """Looping through rounds of roulette."""
    global points
    # current_points: int = points
    i: int = COLOR
    j: int = NUMBER
    s: str = ""
    red: int = 1
    black: int = 0
    # green: int = 2
    print(f"Roulette Round Number: {round_num}")
    cash_bet: int = int(input(f"{player}, enter an amount of money to bet: "))
    # assert cash_bet <= points
    color_bet: str = str(input(f"Enter color to bet on, {player}.[Enter: Black/Red]: "))
    num_bet: int = int(input("Choose a number to bet on: "))
    if cash_bet <= current_points:
        current_points -= cash_bet
        print(f"Round \"{round_num}\" starting in 3 seconds... ")
        time.sleep(k + 1)
        if i == red:
            print("The winning color is Red!")
            s += "Red"
        elif i == black:
            print("The winning color is Black!")
            s += "Black"
        # else:
        #     print("The winning color is Green!")
        #     s += "Green"
        time.sleep(k)
        print("Now let's see what the number is...")
        time.sleep(3)
        print(j)
        if j == num_bet and s == color_bet:
            cash_bet *= 3
            current_points += cash_bet
            print(f"You tripled your money Congratulations!\n Bank Account Balance: {current_points}")
        elif j == num_bet or s == color_bet:
            cash_bet *= 2
            current_points += cash_bet
            print(f"You doubled your money Congratulations!\n Bank Account Balance: {current_points}")
        else:
            print("You lost this round, get back on the table and try again!")
    else:
        print("Bet is too high for your current bank account balance! Try entering a lower amount.")
        time.sleep(k)
    points = current_points
    return current_points
    # what_now()


def what_now() -> None:
    """Giving the player a choice of what to do next."""
    global player
    global m
    play_again: str = (input(f"{player}, would you like to play again?[Yes/No]"))
    if play_again == "Yes":
        if input("Do you want to play 'Roulette' or 'Side Game'?") == "Roulette":
            m += 1
            roulette_round(m, points)
        else:
            side_game()
    elif play_again == "No":
        print(f"Game Over, total amount of money in account: {points}")
    
    
def side_game() -> None:
    """Side game."""
    global points
    dice_one: str = str(randint(1, 6))
    dice_two: str = str(randint(1, 6))
    print(f"Welcome to Dice Guesser, {player}! If you guess the correct value of")
    print(" one die, your money doubles, and if you guess the pair of dice correct")
    print(", your money triples!")
    guess_one: str = input("Guess the value of Die One: ")
    guess_two: str = input("Guess the value of Die Two: ")
    if guess_one == dice_one and guess_two == dice_two:
        print("You guessed both die correct and tripled your money!")
        points *= 3
    elif guess_one == dice_one and guess_two != dice_two:
        print("You guessed die one correctly, and doubled your money!")
        points *= 2
    elif guess_one != dice_one and guess_two == dice_two:
        print("You guessed die two correctly, and doubled your money!")
        points *= 2
    else:
        print(f"Sorry {player}, you guessed both incorrectly and won no money :(")
    print(f"Total money in account after Dice Guesser: {points}")
    main()


if __name__ == "__main__":
    main()
    