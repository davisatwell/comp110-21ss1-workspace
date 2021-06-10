"""Did you pass comp 110? [Test expressions, for..in use wiht dictionary]"""

final_grades: dict[str, float] = {"Davis": 100.0, "Leo": 90.0, "Rhett": 58.0}

def passing_grade(students: dict[str, float]) -> list[str]:
    """Given stident info, who passess?"""
    results: list[str] = []
    for key in students:
        if students[key] > 60:
            results.append(key)
    return results

print(passing_grade(final_grades)) # Output: ['Davis', 'Leo']
