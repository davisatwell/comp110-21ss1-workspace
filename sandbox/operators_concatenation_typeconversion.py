"EX_01 Personal Help Example"

__author__ = "730384155"

msg: str = input("How old are you?: ")
age = int(msg)
fav_num: str = input("What is your favorite number?: ")
fav_num_as_int = int(fav_num)
operation = age ** fav_num_as_int
print(str(operation))