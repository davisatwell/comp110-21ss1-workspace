class PledgePoints:
    """determines who has the most pledge points."""
    names_and_points: dict[str, int] = {}
    def __init__(self, x: dict[str, int]):
        """Initialize Attributes."""
        self.names_and_points = x


    def __maxpp__(self, x: dict[str, int]) -> str:
        """Returns the pledge with most points."""
        i: int = 0
        s: str = ""
        for key in x:
            if x[key] > i:
                i = x[key]
                s = key
        return s

pledge_class: dict[str, int] = {"davis": 450, "hugh": 422, "leo": 273, "gabe": 600, "trey": 402,"rhett": 0, "ty": 523} 

# declared a new PledgePoints object named a
a: PledgePoints
# to give this new PledgePoints object an initial value, we need to call the constructor
a: PledgePoints = PledgePoints(pledge_class)

print(a.__maxpp__(pledge_class))

for key in pledge_class:
    if key == "gabe":
        pledge_class[key] = pledge_class["leo"]

print(pledge_class["gabe"])