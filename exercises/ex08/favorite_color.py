"""A program to determine top favorite colors."""

__author__ = "730384155"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print(favorite_color(color_count))


color_count: dict[str, int] = {"davis": "red", "leo": "red", "rhett": "blue"}
frequency_table: dict[str, int] = {}

def favorite_color(names_and_colors: dict[str, str]) -> str:
    """returns color that appears most in names_and_colors."""
    s: str = ""
    for key in names_and_colors:
        color = names_and_colors[key]
        if color in frequency_table:
            frequency_table[color] += 1
        else:
            frequency_table[color] = 1
    print(frequency_table)
    # for color in frequency_table:
    #     if frequency_table[key] > values:
    #         values = frequency_table[key]
    #s += str(values)
    return s


if __name__ == "__main__":
    main()