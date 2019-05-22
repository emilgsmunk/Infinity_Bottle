"""
The Infinity Bottle project is the brain child of Emil G.S. Munk and Mikkel F. Danneskiold-Samsøe
Published under the MIT License - see license file in repository:

https://github.com/emilgsmunk/Infinity_Bottle.git
"""

import datetime
import json
from tkinter import *
from tkinter.ttk import *

LARGE_FONT = ("Verdana", 12)


class App(Tk):
    def __init__(self, Active_Infinity_Bottle, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.iconbitmap(self, default="clienticon.ico")
        Tk.wm_title(self, "Infinity Bottle")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.Active_Infinity_Bottle = Active_Infinity_Bottle

        self.frames = {}

        for F in (Main_Page, Add_Volume_Page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main_Page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Main_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Header = Label(self, text="Main Page", font=LARGE_FONT)
        Header.pack(pady=10, padx=10)

        Add_Volume_Page_Button = Button(
            self,
            text="Add Bottle",
            command=lambda: controller.show_frame(Add_Volume_Page),
        )
        Add_Volume_Page_Button.pack()

        Temp_Note = Label(self, text="Data visualization will be here...")
        Temp_Note.pack()

        Quit_Button = Button(self, text="QUIT", command=self.quit)
        Quit_Button.pack(side="bottom")


class Add_Volume_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Header = Label(self, text="Add Volume Page", font=LARGE_FONT)
        Header.pack(pady=10, padx=10)

        Main_Page_Button = Button(
            self, text="Main Screen", command=lambda: controller.show_frame(Main_Page)
        )
        Main_Page_Button.pack()

        # ISSUE: Move (lambda) function to controller (App class) to clean up code
        button_add = Button(self, text="Add", command=lambda: self.add_volume_caller(controller))
        button_add.pack()

        Frame_entries = Frame(self)
        Frame_entries.pack()
        Frame_left = Frame(Frame_entries)
        Frame_left.pack(side="left")
        Frame_right = Frame(Frame_entries)
        Frame_right.pack(side="right")

        entry_name = Entry(Frame_right)
        entry_name.pack()
        Label_name = Label(Frame_left, text="Name")
        Label_name.pack()

        entry_age = Entry(Frame_right)
        entry_age.pack()
        Label_age = Label(Frame_left, text="Age")
        Label_age.pack()

        entry_origin = Entry(Frame_right)
        entry_origin.pack()
        Label_origin = Label(Frame_left, text="Origin")
        Label_origin.pack()

        entry_abv = Entry(Frame_right)
        entry_abv.pack()
        Label_abv = Label(Frame_left, text="ABV")
        Label_abv.pack()

        entry_weight_before = Entry(Frame_right)
        entry_weight_before.pack()
        Label_weight_before = Label(Frame_left, text="Weight before adding")
        Label_weight_before.pack()

        entry_weight_after = Entry(Frame_right)
        entry_weight_after.pack()
        Label_weight_after = Label(Frame_left, text="Weight after adding")
        Label_weight_after.pack()

        Quit_Button = Button(self, text="QUIT", command=self.quit)
        Quit_Button.pack(side="bottom")

    def add_volume_caller(self,controller):
        controller.Active_Infinity_Bottle.add_volume(
            str(self.entry_name.get()),
            int(self.entry_age.get()),
            str(self.entry_origin.get()),
            float(self.entry_abv.get()),
            int(self.entry_weight_before.get()),
            int(self.entry_weight_after.get()),
        )


class Infinity_Bottle:
    def __init__(self, name, b_type):
        self.Name = "name"
        self.Started = str(datetime.datetime.now())
        self.Type = "b_type"
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

        # with open('data.txt', 'w') as outfile:  
        #     json.dump(data, outfile)


class Bottle:
    def __init__(self, name, age, origin, abv, weight):
        self.Name = name
        self.Age = age
        self.Origin = origin
        self.abv = abv
        self.Weight = weight

# with open('data.txt') as json_file:  
#     data = json.load(json_file)
# ISSUE: Allow customization
Active_Infinity_Bottle = Infinity_Bottle("Infinity Bottle", "Alcohol")

app = App(Active_Infinity_Bottle)
app.mainloop()
app.destroy()
