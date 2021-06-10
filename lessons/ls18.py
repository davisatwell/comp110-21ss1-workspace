"""Examples of dictionaries."""

# Establish a type with the following syntax.
# dict[key type, value type]
# empty dictionary literal is { }
players: dict[str, int] = {}

# Insert a new key-value pair

players["Brooks"] = 15
# Reference keys inside subscription notation, associated
# values are assigned on RIGHT HAND SIDE of operator
players["Love"] = 2
players["Bacot"] = 4
players["Bacot"] = 5
print(players)

new_dict: dict[str, str] = {"Davis": "blue", "Leo": "red"}
new_dict["Rhett"] = ["Purple"]
print(new_dict)
new_dict.pop("Rhett")
print(new_dict)

for key in new_dict:
    print(f"The key is {key} and the value is {new_dict[key]}") 

# {} - references identifying a dictionary (dictionary paramenter)

for val in new_dict.values():
    print(f"The value is {val}")


final_grades: dict[str, float] = {"Davis": 100.0, "Leo": 90.0, "Rhett": 58.0}

def passing_grade(students: dict[str, float]) -> list[str]:
    """Given stident info, who passess?"""
    results: list[str] = []
    for key in students:
        if students[key] > 60:
            results.append(key)
    return results

print(passing_grade(final_grades)) # Output: ['Davis', 'Leo']
