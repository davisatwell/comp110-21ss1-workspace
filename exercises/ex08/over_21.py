"""A program to determine names over 21."""

__author__ = "730384155"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print(over_21(birthdays_tested))


birthdays_tested: dict[str, int] = {"Davis": 2002, "JT": 1965, "Mason": 2001, "Chris": 1966}


def over_21(names_and_birth_year: dict[str, int]) -> list[str]:
    """Creating a list of students over 21."""
    resulting_list: list[str] = []
    for key in names_and_birth_year:
        if 2021 - names_and_birth_year[key] >= 21:
            resulting_list.append(key)
    return resulting_list


if __name__ == "__main__":
    main()