from __future__ import annotations

class Yikes:
    x: int = 0

    def __add__(self, rhs: Yikes) -> int:
        self.x += rhs
        return self.x

y: Yikes = Yikes()
y.x = 1
z: int = y + 2
print(z)