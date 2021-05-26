"""Magic 8-Ball"""

from random import randint

questions: str = input("Ask the 8-Ball a question:")
number: int = randint(0,2)

# 8-Ball Utilizing "elif" statements
if number == 0:
    print("Very doubtful")
elif number == 1:
    print("Ask again later")
else:
    print("It is certain")

# 8-Ball utilizing nesting
if number == 0:
    print("Very doubtful")
else:
    if number == 1:
        print("Ask again later")
    else:
        print("It is certain")