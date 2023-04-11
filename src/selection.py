import json
import tkinter as tk
from PIL import Image, ImageTk
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path


class Selection:
    def __init__(self, root):
        """
        Selection screen window
        :param root: tkinter window object
        """
        self.root = root
        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        height = resolution_dictionary[self.data["resolution"]][1]

        self.coefficient = height/540

        exercises = Image.open(resource_path("img/text/exercisestitle.png"))
        exercises = exercises.resize((round(420 * self.coefficient), round(100 * self.coefficient)))
        self.exercisesphoto = ImageTk.PhotoImage(exercises)

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = self.exercisesphoto
        GLabel_771.place(x=round(270 * self.coefficient), y=round(30 * self.coefficient),
                         width=round(420 * self.coefficient), height=round(100 * self.coefficient))

        ear = Image.open(resource_path("img/text/ear.png"))
        ear = ear.resize((round(225 * self.coefficient), round(225 * self.coefficient)))
        earphoto = ImageTk.PhotoImage(ear)

        GButton_605 = tk.Button(self.root)
        GButton_605["bg"] = "#f0f0f0"
        GButton_605['bd'] = 0
        GButton_605["fg"] = "#000000"
        GButton_605["justify"] = "center"
        GButton_605["image"] = earphoto
        GButton_605.place(x=round(212 * self.coefficient), y=round(225 * self.coefficient),
                          width=round(225 * self.coefficient), height=round(225 * self.coefficient))
        GButton_605["command"] = self.GButton_605_command

        notation = Image.open(resource_path("img/text/notations.png"))
        notation = notation.resize((round(225 * self.coefficient), round(225 * self.coefficient)))
        notationphoto = ImageTk.PhotoImage(notation)

        GButton_890 = tk.Button(self.root)
        GButton_890["bd"] = 0
        GButton_890["bg"] = "#f0f0f0"
        GButton_890["fg"] = "#000000"
        GButton_890["justify"] = "center"
        GButton_890["image"] = notationphoto
        GButton_890.place(x=round(522 * self.coefficient), y=round(225 * self.coefficient),
                          width=round(225 * self.coefficient), height=round(225 * self.coefficient))
        GButton_890["command"] = self.GButton_890_command

        arrow = Image.open(resource_path("img/back_arrow.png"))
        arrow = arrow.resize((round(122 * self.coefficient), round(122 * self.coefficient)))
        arrowphoto = ImageTk.PhotoImage(arrow)

        GButton_172 = tk.Button(self.root)
        GButton_172["bd"] = 0
        GButton_172["fg"] = "#000000"
        GButton_172["justify"] = "center"
        GButton_172["image"] = arrowphoto
        GButton_172.place(x=round(30 * self.coefficient), y=round(5 * self.coefficient),
                          width=round(122 * self.coefficient), height=round(122 * self.coefficient))
        GButton_172["command"] = self.GButton_172_command

        settingsimg = Image.open(resource_path("img/settings.png"))
        settingsimg = settingsimg.resize((round(122 * self.coefficient), round(122 * self.coefficient)))
        settingsimgphoto = ImageTk.PhotoImage(settingsimg)

        GButton_666 = tk.Button(self.root)
        GButton_666["bd"] = 0
        GButton_666["fg"] = "#000000"
        GButton_666["justify"] = "center"
        GButton_666["image"] = settingsimgphoto
        GButton_666.place(x=round(810 * self.coefficient), y=round(12 * self.coefficient), width=round(122 * self.coefficient), height=round(122 * self.coefficient))
        GButton_666["command"] = self.GButton_666_command
        self.root.mainloop()

    def GButton_666_command(self):
        """
        Switch to Settings screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.settings import Settings
        s = Settings(self.root)

    def GButton_605_command(self):
        """
        Switch to Ear screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.ear import Ear
        e = Ear(self.root)

    def GButton_890_command(self):
        """
        Switch to Notation screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.notation import Notation
        n = Notation(self.root)

    def GButton_172_command(self):
        """
        Switch to App screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.app import App
        a = App(self.root)

