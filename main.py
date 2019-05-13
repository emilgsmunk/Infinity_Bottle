"""
The Infinity Bottle project is the brain child of Emil G.S. Munk and Mikkel F. Danneskiold-Samsøe
Published under the MIT License - see license file in repository:

https://github.com/emilgsmunk/Infinity_Bottle.git
"""

import datetime


class Infinity_Bottle:
    def __init__(self, name):
        self.Name = name
        self.Started = datetime.datetime.now()

    def add_volume(self, weight_before, weight_after, bottle, age, origin, ABV):
        pass


class Bottle:
    def __init__(self, name, brand, ABV):
        pass


# Testing
# ib = Infinity_Bottle("test")

# print(ib.Name)
# print(ib.Started)
