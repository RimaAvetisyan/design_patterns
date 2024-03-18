# Decorator to add blueberries on top of the cake
def add_blueberries(func):
    def wrapper(self):
        func(self)  # Calling the original method
        print("Adding blueberries on top")
    return wrapper

# Decorator to add a chocolate cream layer
def add_chocolate_cream(func):
    def wrapper(self):
        func(self)  # Calling the original method
        print("Adding chocolate cream layer")
    return wrapper

# Applying decorators to the CakeMaker class methods
class CakeMaker:
    @add_blueberries
    @add_chocolate_cream
    def make_base_cake(self):
        print("Making base cake")

# Creating an instance of CakeMaker
baking = CakeMaker()

# Making the decorated cake
baking.make_base_cake()
