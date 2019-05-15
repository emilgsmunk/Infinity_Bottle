"""
The Infinity Bottle project is the brain child of Emil G.S. Munk and Mikkel F. Danneskiold-Samsøe
Published under the MIT License - see license file in repository:

https://github.com/emilgsmunk/Infinity_Bottle.git
"""

import datetime
from tkinter import *


class Infinity_Bottle:
    def __init__(self, master):
        # Bottle related
        self.Name = "name"
        self.Started = str(datetime.datetime.now())
        self.Type = "b_type"
        self.Weight_Total = 0
        self.Weight_Content = 0
        self.Weight_Bottle = 0
        self.Fillings = []
        self.Bottles = {}
        self.add_params = ("name",12,"origin",42,250,350)

        # GUI related
        frame = Frame(master)
        frame.pack()

        self.button_quit = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button_quit.pack(side=LEFT)

        self.button_add = Button(frame, text="Add", command=self.add_volume)
        self.button_add.pack(side=LEFT)

        self.entry_name = Entry(frame)
        self.entry_name.pack()
        self.entry_age = Entry(frame)
        self.entry_age.pack()
        self.entry_origin = Entry(frame)
        self.entry_origin.pack()
        self.entry_abv = Entry(frame)
        self.entry_abv.pack()
        self.entry_weight_before = Entry(frame)
        self.entry_weight_before.pack()
        self.entry_weight_after = Entry(frame)
        self.entry_weight_after.pack()

    def add_volume(self):
        #(name,age, origin, abv, weight_before, weight_after) = self.add_params
        name = str(self.entry_name.get())
        age = int(self.entry_age.get())
        origin = str(self.entry_origin.get())
        abv = float(self.entry_abv.get())
        weight_before = int(self.entry_weight_before.get())
        weight_after = int(self.entry_weight_after.get())

        weight_added = weight_after - weight_before

        if self.Fillings.__len__() == 0:  # For the first filling
            self.Weight_Bottle = weight_before

        else:  # All subsequent fillings
            weight_diff = weight_before - self.Weight_Total

            if weight_diff < 0:  # Content has been consumed
                diff_percent = weight_diff / self.Weight_Content  # Find percentual diff

                for b in self.Bottles:
                    self.Bottles[b].Weight *= 1 + diff_percent

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
        print(self.Fillings)


class Bottle:
    def __init__(self, name, age, origin, abv, weight):
        self.Name = name
        self.Age = age
        self.Origin = origin
        self.abv = abv
        self.Weight = weight




root = Tk()

app = Infinity_Bottle(root)

root.mainloop()
root.destroy()
