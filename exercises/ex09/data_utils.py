"""Data utility functions."""

__author__ = "730384155"

from csv import DictReader

# Functions below are under the hood of pandas and numpy
def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read a CSV file and return a list of its rows."""
    file_handle = open(path, "r", encoding="utf8") # "r" means that this file is only readable
    csv_reader = DictReader(file_handle)
    table: list[dict[str, str]] = []
    for row in csv_reader:
        print(row)
        table.append(row)
    return table

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Return a column's values."""
    values: list[str] = []
    for row in table:
        values.append(row[column])
    return values

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convertng a table of rows to a table of columns."""
    result: dict[str, list[str]] = {}
    keys = table[0].keys()
    for key in keys:
        print(f"The key is {key}")
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Get first n rows."""
    result: dict[str, list[str]] = {}
    for key in table: # looking at date, high, and low
        result[key] = table[key][:rows] # [:rows] makes it so x amount of rows is being extracted from table ([:]) - Slicing
    return result

def select(table: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Select a subset of columns."""
    result: dict[str, list[str]] = {}
    for col_name in cols:
        result[col_name] = table[col_name]
    return result

# table: list[dict[str, str]] = read_csv_rows("data/nc_durham_2015_march_21_to_27.csv")

# column_oriented = columnar(table)
# n_rows = (head(column_oriented, 2)) # OUTPUT: {'date': ['3/16', '3/17'], ' high': [' 48.0', ' 63.0'], ' low': [' 39.0', ' 51.0']}
# print(n_rows) # (head(column_oriented, 2)) is saying that "I want to print the first two rows of data in said CSV file in column oriented format"
# # dates = column_values(table, "date") # extracts the "date" column from the weather.csv file
# # print(dates)
# # high = column_values(table, " high")
# # print(high)

# subset_col_oriented = select(column_oriented, ["date", " low"])
# print(f"Subset of Columns: {subset_col_oriented}")


def count(values: list[str]) -> dict[str, int]:
    """Returning a dictionary of the counts of the items in input list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        elif item not in result:
            result[item] = 1
    return result 