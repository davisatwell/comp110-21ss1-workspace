"""How many years until your 50th bBirthday?"""

curr_age: str = input("How old are you right now? ")
curr_age_int: int = int(curr_age)
fifty: int = curr_age_int + 50-curr_age_int
print(fifty)

years_to_go: int = 50 -curr_age_int
print("You have",years_to_go, "years until you are 50.")
print("You have "+str(years_to_go)+" years until you are 50.")
