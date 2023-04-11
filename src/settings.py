import tkinter as tk
from PIL import Image, ImageTk
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path
import json


class Settings:
    def __init__(self, root):
        """
        Settings window object
        :param root: tkinter window object
        """
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height / 540

        settingstitle = Image.open(resource_path("img/text/settingstitle.png"))
        settingstitle = settingstitle.resize((round(420 * self.coefficient), round(120 * self.coefficient)))
        settingsphoto = ImageTk.PhotoImage(settingstitle)

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = settingsphoto
        GLabel_771.place(x=round(270 * self.coefficient), y=round(15 * self.coefficient), width=round(420 * self.coefficient), height=round(120 * self.coefficient))

        unchecked = Image.open(resource_path("img/text/unchecked.png"))
        unchecked = unchecked.resize((round(60 * self.coefficient), round(60 * self.coefficient)))
        self.uncheckedphoto = ImageTk.PhotoImage(unchecked)

        europeannotation = Image.open(resource_path("img/text/europeannotation.png"))
        europeannotation = europeannotation.resize((round(468 * self.coefficient), round(60 * self.coefficient)))
        self.europeannotationphoto = ImageTk.PhotoImage(europeannotation)

        middle_csettigns = Image.open(resource_path("img/text/middle_csettigns.png"))
        middle_csettigns = middle_csettigns.resize((round(468 * self.coefficient), round(60 * self.coefficient)))
        self.middle_csettignsphoto = ImageTk.PhotoImage(middle_csettigns)

        modes = Image.open(resource_path("img/text/modes.png"))
        modes = modes.resize((round(468 * self.coefficient), round(60 * self.coefficient)))
        self.modesphoto = ImageTk.PhotoImage(modes)

        fs = Image.open(resource_path("img/text/fullscreen.png"))
        fs = fs.resize((round(468 * self.coefficient), round(60 * self.coefficient)))
        self.fsphoto = ImageTk.PhotoImage(fs)

        checked = Image.open(resource_path("img/text/checked.png"))
        checked = checked.resize((round(60 * self.coefficient), round(60 * self.coefficient)))
        self.checkedphoto = ImageTk.PhotoImage(checked)

        self.checkbutton_var = tk.BooleanVar()

        checkbutton = tk.Checkbutton(self.root)
        checkbutton["image"] = self.uncheckedphoto
        checkbutton["bd"] = 0
        checkbutton["justify"] = 'center'
        checkbutton["variable"] = self.checkbutton_var
        checkbutton["command"] = self.europe_notation
        checkbutton["selectimage"] = self.checkedphoto
        checkbutton.place(x=round(656 * self.coefficient), y=round(150 * self.coefficient), width=round(90 * self.coefficient), height=round(60 * self.coefficient))

        if self.data['european_notation']:
            self.checkbutton_var.set(True)

        self.checkbutton_var2 = tk.BooleanVar()

        checkbutton = tk.Checkbutton(self.root)
        checkbutton["image"] = self.uncheckedphoto
        checkbutton["bd"] = 0
        checkbutton["variable"] = self.checkbutton_var2
        checkbutton["command"] = self.modes
        checkbutton["selectimage"] = self.checkedphoto
        checkbutton.place(x=round(656 * self.coefficient), y=round(250 * self.coefficient), width=round(90 * self.coefficient), height=round(60 * self.coefficient))

        if self.data['modes']:
            self.checkbutton_var2.set(True)

        self.checkbutton_var3 = tk.BooleanVar()

        checkbutton = tk.Checkbutton(self.root)
        checkbutton["image"] = self.uncheckedphoto
        checkbutton["bd"] = 0
        checkbutton["variable"] = self.checkbutton_var3
        checkbutton["command"] = self.middle_c
        checkbutton["selectimage"] = self.checkedphoto
        checkbutton.place(x=round(656 * self.coefficient), y=round(350 * self.coefficient), width=round(90 * self.coefficient), height=round(60 * self.coefficient))

        if self.data['middle_c']:
            self.checkbutton_var3.set(True)

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = self.europeannotationphoto
        GLabel_771.place(x=round(207 * self.coefficient), y=round(150 * self.coefficient), width=round(468 * self.coefficient), height=round(60 * self.coefficient))

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = self.modesphoto
        GLabel_771.place(x=round(207 * self.coefficient), y=round(250 * self.coefficient), width=round(468 * self.coefficient), height=round(60 * self.coefficient))

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = self.middle_csettignsphoto
        GLabel_771.place(x=round(207 * self.coefficient), y=round(350 * self.coefficient), width=round(468 * self.coefficient), height=round(60 * self.coefficient))

        arrow = Image.open(resource_path("img/back_arrow.png"))
        arrow = arrow.resize((round(122 * self.coefficient), round(122 * self.coefficient)))
        arrowphoto = ImageTk.PhotoImage(arrow)

        GButton_172 = tk.Button(self.root)
        GButton_172["bd"] = 0
        GButton_172["fg"] = "#000000"
        GButton_172["justify"] = "center"
        GButton_172["image"] = arrowphoto
        GButton_172.place(x=round(30 * self.coefficient), y=round(5 * self.coefficient), width=round(122 * self.coefficient), height=round(122 * self.coefficient))
        GButton_172["command"] = self.GButton_172_command

        self.checkbutton_var4 = tk.BooleanVar()

        checkbutton = tk.Checkbutton(self.root)
        checkbutton["image"] = self.uncheckedphoto
        checkbutton["bd"] = 0
        checkbutton["justify"] = 'center'
        checkbutton["variable"] = self.checkbutton_var4
        checkbutton["command"] = self.fullscreen
        checkbutton["selectimage"] = self.checkedphoto
        checkbutton.place(x=round(656 * self.coefficient), y=round(450 * self.coefficient),
                          width=round(90 * self.coefficient), height=round(60 * self.coefficient))

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = self.fsphoto
        GLabel_771.place(x=round(207 * self.coefficient), y=round(450 * self.coefficient),
                         width=round(468 * self.coefficient), height=round(60 * self.coefficient))

        if self.data['resolution'] == 'fullscreen':
            self.checkbutton_var4.set(True)

        self.root.mainloop()

    def GButton_172_command(self):
        """
        Switch to Selection screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.selection import Selection
        s = Selection(self.root)

    def fullscreen(self):
        """
        Toggle between Fullscreen and 960x540
        """
        if self.checkbutton_var4.get():
            with open(resource_path("settings/settings.json"), 'w') as st:
                self.data['resolution'] = 'fullscreen'
                st.write(json.dumps(self.data))
        else:
            with open(resource_path("settings/settings.json"), 'w') as st:
                self.data['resolution'] = '960'
                st.write(json.dumps(self.data))

        self.root.destroy()
        from main import main
        main(True)

    def europe_notation(self):
        """
        Toggle between european notation and western notation
        """
        if self.checkbutton_var.get():
            with open(resource_path("settings/settings.json"), 'w') as st:
                self.data['european_notation'] = True
                st.write(json.dumps(self.data))
        else:
            with open(resource_path("settings/settings.json"), 'w') as st:
                self.data['european_notation'] = False
                st.write(json.dumps(self.data))

    def modes(self):
        """
        Enable modes on Key signature exercise
        """
        if self.checkbutton_var2.get():
            with open(resource_path("settings/settings.json"), 'w') as st:
                self.data['modes'] = True
                st.write(json.dumps(self.data))
        else:
            with open(resource_path("settings/settings.json"), 'w') as st:
                self.data['modes'] = False
                st.write(json.dumps(self.data))

    def middle_c(self):
        """
        Toggle middle C4 for Note ear exercise
        """
        if self.checkbutton_var3.get():
            with open(resource_path("settings/settings.json"), 'w') as st:
                self.data['middle_c'] = True
                st.write(json.dumps(self.data))
        else:
            with open(resource_path("settings/settings.json"), 'w') as st:
                self.data['middle_c'] = False
                st.write(json.dumps(self.data))
