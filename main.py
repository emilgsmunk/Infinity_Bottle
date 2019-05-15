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
        self.Started = str(datetime.datetime.now())
        self.Type = b_type
        self.Weight_Total = 0
        self.Weight_Content = 0
        self.Weight_Bottle = 0
        self.Fillings = []
        self.Bottles = {}

    def add_volume(self, name, age, origin, abv, weight_before, weight_after):

        weight_added = weight_after - weight_before

        if self.Fillings.__len__() == 0:  # For the first filling
            self.Weight_Bottle = weight_before

        else:  # All subsequent fillings
            weight_diff = weight_before - self.Weight_Total

            if weight_diff < 0:  # Content has been consumed
                diff_percent = weight_diff / self.Weight_Content  # Find percentual diff

                for b in self.Bottles:
                    self.Bottles[b].Weight *= (1 + diff_percent)

            elif weight_diff > 0:
                print("ERROR: Weight has increased!")
                quit()
            
        self.Weight_Total = weight_after
        self.Weight_Content = self.Weight_Total - self.Weight_Bottle

        if name + "_" + str(age) not in self.Bottles:
            self.Bottles[name + "_" + str(age)] = Bottle(
                name, age, origin, abv, weight_added
            )
        else:
            self.Bottles[name + "_" + str(age)].Weight += weight_added

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


class Bottle:
    def __init__(self, name, age, origin, abv, weight):
        self.Name = name
        self.Age = age
        self.Origin = origin
        self.abv = abv
        self.Weight = weight


# Testing
# ib = Infinity_Bottle("test")

# print(ib.Name)
# print(ib.Started)

# IB_name = input("enter name of Infinity Bottle: \n")
# IB_type = input("enter type of Infinity Bottle: \n")
IB_name = "test name"
IB_type = "test type"

IB = Infinity_Bottle(IB_name, IB_type)

# IB.add_volume("name", 12, "origin", 42, 250, 350)
# IB.add_volume("name2", 10, "origin2", 50, 300, 450)
# IB.add_volume("name", 12, "origin", 42, 350, 450)


# root = Tk()

# button_add = Button(
#             root, text="Add", command=print("yay!")
#             )
# button_add.pack(side=RIGHT)
# label_test = Label(root,text=IB.Fillings.__len__())
# label_test.pack(side=LEFT)

# root.mainloop()


# from Tkinter import *

# class App:

#     def __init__(self, master):

#         frame = Frame(master)
#         frame.pack()

#         self.button = Button(
#             frame, text="QUIT", fg="red", command=frame.quit
#             )
#         self.button.pack(side=LEFT)

#         self.hi_there = Button(frame, text="Hello", command=self.say_hi)
#         self.hi_there.pack(side=LEFT)

#     def say_hi(self):
#         print "hi there, everyone!"

# root = Tk()

# app = App(root)

# root.mainloop()
# root.destroy() # optional; see description below