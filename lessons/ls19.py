"""Practicing with CSVs."""

from csv import DictReader

file_handle = open("data/weather.csv", encoding="utf8")
csv_reader = DictReader(file_handle)


table: list[dict[str, str]] = []
for row in csv_reader:
    print(row)
    table.append(row)

print(table)
