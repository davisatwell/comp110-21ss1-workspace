"""Unluck 13 Number Guesser."""

print("Guess a number!")

guess: int = int(input("Guess: "))

# Non simplified Program
if guess == 13:
    print("Correct!")
else:
    if guess == 12:
        print("SO close, add 1!")
    else:
        if guess > 13:
            print("lower")
        else:
            if guess < 13:
                print("higher")

print("Game Over")

# Simplified program using "elif" statements
if guess == 13:
    print("Correct!")
elif guess == 12:
    print("SO close, add 1!")
elif guess > 13:
    print("lower")
else:
    print("higher")

print("Game Over")

# Reassignment