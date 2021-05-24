"""A vaccination calculator."""

__author__ = "730384155"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta

# Global Vars needed for calculator
population_input: str = input("Population: ")
population: int = int(population_input)
# Note: 2 doses will cover one person
doses_administered_input: str = input("Doses administered: ")
doses_administered: int = int(doses_administered_input)
doses_per_day_input: str = input("Doses per day: ")
doses_per_day: int = int(doses_per_day_input)
target_percent_vaccinated_input: str = input("Target percent vaccinated: ")
target_percent_vaccinated: int = int(target_percent_vaccinated_input)
today: datetime = datetime.today()
one_day: timedelta = timedelta(1)
# Start of program
dec_target: float = target_percent_vaccinated / 100
target_doses: float = population * dec_target
target_doses1: float = target_doses * 2
target_doses2: float = target_doses1 - doses_administered
days_to_goal: int = round(target_doses2 / doses_per_day)
days_to_goal1: timedelta = timedelta(days_to_goal)
day_goal_is_reached: datetime = today + days_to_goal1
date_: str = day_goal_is_reached.strftime("%B %d, %Y")
prcnt: str = str(target_percent_vaccinated)
days: str = str(days_to_goal)
date: str = str(date_)
print("We will reach", prcnt + "%", "vaccination in", days, "days, which falls on", date)