"""
The Infinity Bottle project is the brain child of Emil G.S. Munk and Mikkel F. Danneskiold-Samsøe
Published under the MIT License - see license file in repository:

https://github.com/emilgsmunk/Infinity_Bottle.git
"""

import datetime


class Infinity_Bottle:
    """
    The Infinity_Bottle class is the main class for the application. This will hold information about the Infinity Bottle itself, such as name, creation time, type (e.g. whisky or rum), etc.
    """

    def __init__(self, name, b_type):
        self.Name = name
        self.Started = datetime.datetime.now()
        self.Type = b_type
        self.Fillings = []
        self.Contents = []
        self.Bottles = {}

    def add_volume(self, name, age, origin, abv, weight_before, weight_after):
        self.Fillings.append(
            [
                str(datetime.datetime.now()),
                name,
                age,
                origin,
                abv,
                weight_before,
                weight_after,
            ]
        )
        # ISSUE: Update Contents here

        if name + "_" + str(age) not in self.Bottles:
            self.Bottles[name + "_" + str(age)] = Bottle(name, age, origin, abv)


class Bottle:
    def __init__(self, name, age, origin, abv):
        self.Name = name
        self.Age = age
        self.Origin = origin
        self.abv = abv


# Testing
# ib = Infinity_Bottle("test")

# print(ib.Name)
# print(ib.Started)

IB = Infinity_Bottle("Tester", "Rum")

IB.add_volume("name", 12, "origin", 42, 250, 350)

print("Done")
