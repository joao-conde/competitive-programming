import math


class SquarePeg:
    def __init__(self, width: float):
        self.width = width


class RoundPeg:
    def __init__(self, radius: float):
        self.radius = radius


class RoundHole:
    def __init__(self, radius: float):
        self.radius = radius

    def fits(self, peg: RoundPeg):
        return self.radius >= peg.radius


class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg: SquarePeg):
        self.square_peg = square_peg
        self.radius = self.square_peg.width * math.sqrt(2) / 2


hole = RoundHole(2.5)
peg1 = RoundPeg(2.1)
peg2 = SquarePeg(2)

hole.fits(peg1)
hole.fits(SquarePegAdapter(peg2))
