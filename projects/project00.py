"""Roulette Simulator"""

__author__: str
__author__ = "730384155"

# Imports

import time
import random
from random import randint

# Globals
zero: int = 0
one: int = 1
k: int = 2  
player: str = ""
points: int = 50
color_generator: list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
number_range: list = list(range(-1,37))
range_1: list = list(range(0,11)) # Odd numbers are RED and even numbers are BLACK.
range_2: list = list(range(18,29)) # Odd numbers are RED and even numbers are BLACK.
range_3: list = list(range(10, 19))# Odd numbers are BLACK and even numbers are RED.
range_4: list = list(range(28, 37))# Odd numbers are BLACK and even numbers are RED.
COLOR: int = random.choice(color_generator)
NUMBER: int = random.choice(number_range)
T: bool = True
F: bool = False

def main() -> None:
    global points
    m: int = 1
    greet()
    time.sleep(k+1)
    roulette_round(m,points)
    what_now()
    
    

def greet() -> None:
    player_input: str = input(f"Type \"Start\" and press return to begin: ")
    if player_input == "Start" or "start":
            global player
            print("Welcome to the Old Well Casino!")
            time.sleep(k)
            print(f"Today we will be playing Roulette.\n Esentially, you will start off with a set amount of money. \n When prompted, you will place a bet of any amount your bank account will allow for on a single number or group of numbers. \n If one of your guessed number/numbers matches up with the winning number revealed by the dealer, then your money goes up! \n Let's see if you know when to walk away from the table.")
            time.sleep(k)
            print("You are staring off with $50, so make sure your first bet is equal to or below that value.")
            name_input: str = input("Enter your player name: ")
            player += name_input
    else:
            print("Nice spelling, try again.")
            time.sleep(k + 1)
            greet()


def roulette_round(round_num: int, current_points: int) -> int:
    """Looping through rounds of roulette."""
    global points
    current_points: int = points
    i: int = COLOR
    j: int = NUMBER
    s: str = ""
    red: int = 1
    black: int = 0
    green: int = 2
    cash_bet: int = int(input("Enter an amount of money to bet: "))
    color_bet: str = str(input("Enter the color you wish to bet on (Black, Red, Green (CASE SENSITIVE- enter how written)): "))
    num_bet: int = int(input("Choose a number to bet on: "))
    if cash_bet <= current_points:
        points -= cash_bet
        print(f"Round \"{round_num}\" starting in 3 seconds... ")
        time.sleep(k+1)
        if i == red:
            print("The winning color is Red!")
            s += "Red"
        elif i == black:
            print("The winning color is Black!")
            s += "Black"
        else:
            print("The winning color is Green!")
            s += "Green"
        time.sleep(k)
        print("Now let's see what the number is...")
        time.sleep(3)
        print(j)
        if j == num_bet and s == color_bet:
            points *= 3
            print(f"You tripled your money Congratulations!\n Bank Account Balance: {points}")
            return points
        elif j == num_bet or s == color_bet:
            points *= 2
            print(f"You doubled your money Congratulations!\n Bank Account Balance: {points}")
            return points
        else:
            print("You lost this round, get back on the table and try again!")
            return points
    else:
        print("Bet is too high for your current bank account balance! Try entering a lower amount.")
        time.sleep(k)
        return points

def what_now() -> None:
    print("Play again?")

if __name__ == "__main__":
    main()
    