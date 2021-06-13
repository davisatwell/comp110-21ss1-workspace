"""A class to model a basketball game."""

__author__ = "730384155"


class BBallGame:
    """Winner of a basketball game."""
    biscuits: bool
    points: int
    winning_team: str 
    losing_team: str 

    def __init__(self, p: int, wt: str, lt: str):
        """Initializing attributes."""
        self.points = p
        self.winning_team = wt
        self.losing_team = lt
        self.biscuits = False

    def check_points(self) -> None:
        """Do we get biscuits."""
        if self.points >= 100:
            self.biscuits = True
        return None

    def winner(self) -> str:
        """Winning team of BBall game."""
        if self.winning_team == "UNC" and self.losing_team == "Dook":
            return "GTHD!!"
        elif self.winning_team == "UNC":
            return "woohoo"
        else:
            return "daggum"

    def reset_points(self) -> int:
        """Reset the amount of points the winner had."""
        prev_points: int = self.points
        self.points = 0
        return prev_points
        
