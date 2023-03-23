class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def build(self):
        return self.burger

    def add_buns(self, buns):
        self.burger.buns = buns
        return self

    def add_patty(self, patty):
        self.burger.patty = patty
        return self


builder = BurgerBuilder()
burger = (
    builder.add_buns(["sesame seed bun", "wheat bun"]).add_patty("lean beef").build()
)
