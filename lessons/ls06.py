"""While Loop Demo"""

iterations: int = int(input("How many times do you want to loop?: "))

i: int = 0
while i < iterations:
    print("In repeat block")
    print("i is " + str(i))
    i += 1

print("After repeat block")
print("i's final value is: " + str(i))