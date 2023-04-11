import tkinter as tk
from PIL import Image, ImageTk
from vendor.rp import resource_path
import json
from src.dict.res_dict import resolution_dictionary


class App:
    def __init__(self, root):
        """
        Main menu screen
        :param root: tkinter window
        """
        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())
        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]

        self.coefficient = height/540

        image = Image.open(resource_path("img/theorite.png"))
        image = image.resize((round(473 * self.coefficient), round(200 * self.coefficient)))
        photo = ImageTk.PhotoImage(image)

        GLabel_359 = tk.Label(self.root)
        GLabel_359["image"] = photo
        GLabel_359["fg"] = "#333333"
        GLabel_359["justify"] = "center"
        GLabel_359.place(x=round(240 * self.coefficient), y=round((10 * self.coefficient)), width=round(473 * self.coefficient), height=round(200 * self.coefficient))

        profile = Image.open(resource_path("img/profile.png"))
        profile = profile.resize((round(122 * self.coefficient), round(122 * self.coefficient)))
        profilephoto = ImageTk.PhotoImage(profile)

        GLabel_536 = tk.Button(self.root)
        GLabel_536["fg"] = "#333333"
        GLabel_536["bd"] = 0
        GLabel_536["justify"] = "center"
        GLabel_536["command"] = self.prof
        GLabel_536["image"] = profilephoto
        GLabel_536.place(x=round(790 * self.coefficient), y=round(15 * self.coefficient), width=round(122 * self.coefficient), height=round(122 * self.coefficient))

        exercises = Image.open(resource_path("img/text/exercises.png"))
        exercises = exercises.resize((round(446 * self.coefficient), round(189 * self.coefficient)))
        exercisesphoto = ImageTk.PhotoImage(exercises)

        GButton_636 = tk.Button(self.root)
        GButton_636["bg"] = "#f0f0f0"
        GButton_636['bd'] = 0
        GButton_636["fg"] = "#f0f0f0"
        GButton_636["justify"] = "center"
        GButton_636["image"] = exercisesphoto
        GButton_636.place(x=round(260 * self.coefficient), y=round(210 * self.coefficient), width=round(446 * self.coefficient), height=round(189 * self.coefficient))
        GButton_636["command"] = self.GButton_636_command

        GLabel_73 = tk.Label(self.root)
        GLabel_73["fg"] = "#333333"
        GLabel_73["justify"] = "center"
        GLabel_73["text"] = "made by Deniel Stájner"
        GLabel_73.place(x=round(800 * self.coefficient), y=round(500 * self.coefficient), width=round(160 * self.coefficient), height=(30 * self.coefficient))

        quitimg = Image.open(resource_path("img/quit.png"))
        quitimg = quitimg.resize((round(122 * self.coefficient), round(122 * self.coefficient)))
        quitphoto = ImageTk.PhotoImage(quitimg)

        GButton_172 = tk.Button(self.root)
        GButton_172["bd"] = 0
        GButton_172["fg"] = "#000000"
        GButton_172["justify"] = "center"
        GButton_172["image"] = quitphoto
        GButton_172.place(x=round(30 * self.coefficient), y=round(10 * self.coefficient), width=round(122 * self.coefficient), height=round(122 * self.coefficient))
        GButton_172["command"] = self.quit

        self.root.mainloop()

    def quit(self):
        """
        Quit window
        """
        self.root.destroy()

    def GButton_636_command(self):
        """
        Switch to Selection screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.selection import Selection
        s = Selection(self.root)

    def prof(self):
        """
        Switch to Profile screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.profile import Profile
        p = Profile(self.root)
