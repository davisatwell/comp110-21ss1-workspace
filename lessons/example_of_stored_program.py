"""This file was used during class on May 20th"""

print("Happy Thursday!")

x = "hello"
print(x)
print("The first value in the string assigned to varible x is " + x[0])

#Combining Operators
division: float = 7/5
modulo: int = 7%5
print("The value of the var division is", division)
print("The value of modulo is", modulo)

print(division + modulo)
print(division/modulo)
print(division//modulo)
x: float = (division**modulo) #this one produces a rounding error! (proof computer's memory has limitations)
y: float = float(x)
print(y)
print(division%modulo)

#Variables

#Var reassignment
x = 4
print(x) #prints 4
x = "davis" 
print(x) #this same command from line 2 now prints "davis"

t: str
t = "hi"
g = t + str(1)
print(g)

age: int
age = 12
print(age)
age: str
age = "13"
print(age)
