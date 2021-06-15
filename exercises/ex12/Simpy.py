"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730384155"


class Simpy:
    """Simpy Class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize Attributes."""
        self.values = values

    def __repr__(self) -> str:
        """Represent Simpy object as output."""
        return f"Simpy({self.values})"

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator Overloading +."""
        new_simpy_object: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert range(len(self.values)) == range(len(rhs.values))
            for e in range(len(self.values)):
                new_simpy_object[e].values.append(self.values[e] + rhs.values[e])
        elif isinstance(rhs, float):
            for item in self.values:
                new_simpy_object.values.append(item + rhs)
        return new_simpy_object

    def __getitem__(self, rhs: int) -> float:
        """Enabling Subscription Notation with Simpy class type."""
        return self.values[rhs]
                
    def fill(self, element_: float, num: int) -> None:
        """Fill."""
        i: int = 0
        self.values = []
        while i < num:
            self.values.append(element_)
            i += 1