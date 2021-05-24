"""Vax Calc"""

from datetime import datetime, timedelta

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
#Start of program
dec_target: float = target_percent_vaccinated/100
target_doses: float = population*dec_target
#target_doses: int = round(target_doses)
#doses_to_reach_goal: int = target_doses - doses_administered
days_to_goal: float = target_doses/doses_per_day
print(days_to_goal)
days_to_goal1: int = round(days_to_goal)
print(days_to_goal)
days_to_goal: timedelta = timedelta(days_to_goal1)
print(days_to_goal)
day_goal_is_reached: datetime = today + days_to_goal
date_: str = day_goal_is_reached.strftime("%B %d, %Y")

print("We will reach",str(target_percent_vaccinated)+"%","vaccination in",str(days_to_goal1),"days, which falls on", date_)