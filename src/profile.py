import tkinter as tk
from PIL import Image, ImageTk
import json
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path


class Profile:
    def __init__(self, root):
        """
        Profile window object
        :param root: tkinter window object
        """
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height/540

        ear = Image.open(resource_path("img/text/eartraining.png"))
        ear = ear.resize((round(400 * self.coefficient), round(85 * self.coefficient)))
        earphoto = ImageTk.PhotoImage(ear)

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = earphoto
        GLabel_771.place(x=round(50 * self.coefficient), y=round(150 * self.coefficient), width=round(400 * self.coefficient), height=round(85 * self.coefficient))

        notation = Image.open(resource_path("img/text/notationtraining.png"))
        notation = notation.resize((round(370 * self.coefficient), round(85 * self.coefficient)))
        notationphoto = ImageTk.PhotoImage(notation)

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = notationphoto
        GLabel_771.place(x=round(510 * self.coefficient), y=round(150 * self.coefficient), width=round(370 * self.coefficient), height=round(85 * self.coefficient))

        stats = Image.open(resource_path("img/text/stats.png"))
        stats = stats.resize((round(414 * self.coefficient), round(80 * self.coefficient)))
        statsphoto = ImageTk.PhotoImage(stats)

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = statsphoto
        GLabel_771.place(x=round(273 * self.coefficient), y=round(30 * self.coefficient), width=round(414 * self.coefficient), height=round(80 * self.coefficient))

        rst = Image.open(resource_path("img/text/reset.png"))
        rst = rst.resize((round(79 * self.coefficient), round(45 * self.coefficient)))
        self.rstphoto = ImageTk.PhotoImage(rst)

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Note: {self.stats['note_ear'][0]}/{self.stats['note_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(70 * self.coefficient), y=round(250 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        btn = tk.Button(self.root)
        btn["image"] = self.rstphoto
        btn["bd"] = 0
        btn["command"] = lambda: self.reset('note_ear')
        btn.place(x=round(350 * self.coefficient), y=round(250 * self.coefficient), width=round(79 * self.coefficient), height=round(45 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Interval: {self.stats['interval_ear'][0]}/{self.stats['interval_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(70 * self.coefficient), y=round(300 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        btn = tk.Button(self.root)
        btn["image"] = self.rstphoto
        btn["bd"] = 0
        btn["command"] = lambda: self.reset('interval_ear')
        btn.place(x=round(350 * self.coefficient), y=round(300 * self.coefficient), width=round(79 * self.coefficient), height=round(45 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Scale: {self.stats['scale_ear'][0]}/{self.stats['scale_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(70 * self.coefficient), y=round(350 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        btn = tk.Button(self.root)
        btn["image"] = self.rstphoto
        btn["bd"] = 0
        btn["command"] = lambda: self.reset('scale_ear')
        btn.place(x=round(350 * self.coefficient), y=round(350 * self.coefficient), width=round(79 * self.coefficient), height=round(45 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Chord: {self.stats['chord_ear'][0]}/{self.stats['chord_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(70 * self.coefficient), y=round(400 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        btn = tk.Button(self.root)
        btn["image"] = self.rstphoto
        btn["bd"] = 0
        btn["command"] = lambda: self.reset('chord_ear')
        btn.place(x=round(350 * self.coefficient), y=round(400 * self.coefficient), width=round(79 * self.coefficient), height=round(45 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Note: {self.stats['note_note'][0]}/{self.stats['note_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(540 * self.coefficient), y=round(250 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        btn = tk.Button(self.root)
        btn["image"] = self.rstphoto
        btn["bd"] = 0
        btn["command"] = lambda: self.reset('note_note')
        btn.place(x=round(820 * self.coefficient), y=round(250 * self.coefficient), width=round(79 * self.coefficient), height=round(45 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Interval: {self.stats['interval_note'][0]}/{self.stats['interval_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(540 * self.coefficient), y=round(300 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        btn = tk.Button(self.root)
        btn["image"] = self.rstphoto
        btn["bd"] = 0
        btn["command"] = lambda: self.reset('interval_note')
        btn.place(x=round(820 * self.coefficient), y=round(300 * self.coefficient), width=round(79 * self.coefficient), height=round(45 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Key signature: {self.stats['key_note'][0]}/{self.stats['key_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(540 * self.coefficient), y=round(350 * self.coefficient), width=round(270 * self.coefficient), height=round(50 * self.coefficient))

        btn = tk.Button(self.root)
        btn["image"] = self.rstphoto
        btn["bd"] = 0
        btn["command"] = lambda: self.reset('key_note')
        btn.place(x=round(820 * self.coefficient), y=round(350 * self.coefficient), width=round(79 * self.coefficient), height=round(45 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Chord: {self.stats['chord_note'][0]}/{self.stats['chord_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(540 * self.coefficient), y=round(400 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        btn = tk.Button(self.root)
        btn["image"] = self.rstphoto
        btn["bd"] = 0
        btn["command"] = lambda: self.reset('chord_note')
        btn.place(x=round(820 * self.coefficient), y=round(400 * self.coefficient), width=round(79 * self.coefficient), height=round(45 * self.coefficient))

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

        self.root.mainloop()

    def GButton_172_command(self):
        """
        Switch to App screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.app import App
        a = App(self.root)

    def reset(self, exercise: str):
        """
        Reset counter for exercise
        :param exercise: Exercise in question
        """
        with open(resource_path('profile/account.json'), 'w') as ex:
            self.stats[exercise] = [0, 0]
            ex.write(json.dumps(self.stats))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Note: {self.stats['note_ear'][0]}/{self.stats['note_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(70 * self.coefficient), y=round(250 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Interval: {self.stats['interval_ear'][0]}/{self.stats['interval_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(70 * self.coefficient), y=round(300 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Scale: {self.stats['scale_ear'][0]}/{self.stats['scale_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(70 * self.coefficient), y=round(350 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Chord: {self.stats['chord_ear'][0]}/{self.stats['chord_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(70 * self.coefficient), y=round(400 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Note: {self.stats['note_note'][0]}/{self.stats['note_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(540 * self.coefficient), y=round(250 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Interval: {self.stats['interval_note'][0]}/{self.stats['interval_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(540 * self.coefficient), y=round(300 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Key signature: {self.stats['key_note'][0]}/{self.stats['key_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(540 * self.coefficient), y=round(350 * self.coefficient), width=round(270 * self.coefficient), height=round(50 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root, font=("Calibri", round(18 * self.coefficient)), anchor='w')
        self.GLabel_27["justify"] = "left"
        self.GLabel_27["text"] = str(f"Chord: {self.stats['chord_note'][0]}/{self.stats['chord_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(540 * self.coefficient), y=round(400 * self.coefficient), width=round(200 * self.coefficient), height=round(50 * self.coefficient))


