"""Number Guesser."""

print("Guess a number!")

guess: int = int(input("Guess: "))

if guess == 13:
    print("Correct!")
else:
    print("Incorrect!")

print("Game Over")
