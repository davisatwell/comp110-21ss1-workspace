"""Practicing with CSVs."""

from csv import DictReader

file_handle = open("data/weather.csv", encoding="utf8")
csv_reader = DictReader(file_handle)

# a table can be modeled as a list of rows
# where each row is a dictionary with the column totle as the key
table: list[dict[str, str]] = [] #represents entire file in a list
for row in csv_reader:
    print(row)
    table.append(row)

print(table)

file_handle.close()

# let's calculate the average high temp
# process the table by a specific column
high_temps: list[float] = []
for row in table:
    high: float = float(row[" high"])
    high_temps.append(high)

print(f"The high temps were {high_temps}")

avg_high: float = 0.0

for e in high_temps:
    avg_high += e
avg_high /= len(high_temps)

print(f"The average high is {avg_high}.")

#OR
print("The average high was: ")
print(avg_high)

#OR you can find the average high the easy way idiot:

average_high: float = sum(high_temps) / len(high_temps)

print(f"The average high is {average_high}.")

