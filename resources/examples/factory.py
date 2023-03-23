class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients


class BurgerFactory:
    @classmethod
    def create_cheese_burger(cls):
        return Burger(["bun", "cheese", "beef-patty"])

    @classmethod
    def create_deluxe_burger(cls):
        return Burger(["bun", "cheese", "beef-patty", "tomatoe", "lettuce"])


cheese = BurgerFactory.create_cheese_burger()
deluxe = BurgerFactory.create_deluxe_burger()
print(cheese.ingredients, deluxe.ingredients)
