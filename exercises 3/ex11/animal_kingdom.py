"""A program that explores the animal kingdom."""
from __future__ import annotations
__author__ = "YOUR 9-DIGIT PID"

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 3: Uncomment the following lines to test your classes
    lion = Animal("lion", 10, "\U0001F981")
    pig = Animal("pig", 3, "\U0001F437")
    ram = Animal("ram", 6, "\U0001F40F")
    elephant = Animal("elephant", 9, "\U0001F418")
    gorilla = Animal("gorilla", 7, "\U0001F98D")
    camel = Animal("camel", 4, "\U0001F42A")

    team1 = Team("Hello Kitty", [lion, ram, pig])
    team2 = Team("BIG", [elephant, gorilla, camel])

    winners = team1.battle(team2)

    print(f"{team1.team_name} vs {team2.team_name}")

    for i in range(len(team1.animals)):
        print(f"{team1.animals[i].emoji}  vs {team2.animals[i].emoji}")
        print(f"The {winners[i].species} wins!")

    print(team1.who_won(team2))


class Animal:
    species: str
    danger_level: int
    emoji: str
    def __init__(self, species: str, danger_level: int, emoji: str):
        """Initializing attributes."""
        self.species = species
        self.danger_level = danger_level
        self.emoji = emoji

    def fight(self, opponent: Animal) -> Animal:
        """Fight of Animals."""
        if self.danger_level > opponent.danger_level:
            return self
        elif self.danger_level == opponent.danger_level:
            return opponent
        else:
            return opponent

class Team:
    """Animal Team."""
    team_name: str
    animals: list[Animal]
    score: int

    def __init__(self, team_name: str, animals: list[Animal]):
        """Initialize Attributes."""
        self.team_name = team_name
        self.animals = animals
        self.score = 0
    
    def battle(self, opponent: Team) -> list[Animal]:
        """The battle of animals in teams of 2."""
        winners: list[Animal] = []
        if len(self.animals) != len(opponent.animals):
            empty_list: list[Animal] = []
            return empty_list
        for element in self.animals and opponent.animals:
            i: int = 0
            animal1: Animal = self.animals[i]
            animal2: Animal = opponent.animals[i]
            if animal1.danger_level > animal2.danger_level:
                self.score += 5
                winners.append(animal1)
            elif animal2.danger_level > animal1.danger_level:
                opponent.score += 5
                winners.append(animal2)
            while i < len(self.animals) and len(opponent.animals):
                i += 1
        return winners
    
    def who_won(self, opponent: Team) -> str:
        """Returns the winning team."""
        if self.score and opponent.score == 0:
            return "The battle hasn't happened yet"
        elif self.score == opponent.score:
            return "It was a tie!"
        elif self.score > opponent.score:
            return f"Team {self.name} won!"
        else:
            return f"Team {opponent.name} won!"

if __name__ == "__main__":
    main()