class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=260),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=350),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=150),
            MenuItem(name="americano", water=200, milk=0, coffee=20, cost=220),
            MenuItem(name="mocha", water=50, milk=100, coffee=18, cost=180),
            MenuItem(name="frappucino", water=0, milk=150, coffee=24, cost=350)
        ]
    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.cost}/"
        return options

a = Menu()
print(a.get_items())