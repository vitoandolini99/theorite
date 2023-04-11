import json
import tkinter as tk
from PIL import Image, ImageTk
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path


class Notation:
    def __init__(self, root):
        """
        Notation screen object
        :param root: tkinter window object
        """
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height/540

        exercises = Image.open(resource_path("img/text/notationtraining.png"))
        exercises = exercises.resize((round(450 * self.coefficient), round(103 * self.coefficient)))
        exercisesphoto = ImageTk.PhotoImage(exercises)

        GLabel_771 = tk.Label(self.root)
        GLabel_771["fg"] = "#333333"
        GLabel_771["justify"] = "center"
        GLabel_771["image"] = exercisesphoto
        GLabel_771.place(x=round(255 * self.coefficient), y=round(30 * self.coefficient), width=round(450 * self.coefficient), height=round(103 * self.coefficient))

        note = Image.open(resource_path("img/text/note.png"))
        note = note.resize((round(300 * self.coefficient), round(100 * self.coefficient)))
        notephoto = ImageTk.PhotoImage(note)

        GButton_181 = tk.Button(self.root)
        GButton_181['bd'] = 0
        GButton_181["bg"] = "#f0f0f0"
        GButton_181["fg"] = "#000000"
        GButton_181["justify"] = "center"
        GButton_181["image"] = notephoto
        GButton_181.place(x=round(140 * self.coefficient), y=round(200 * self.coefficient), width=round(300 * self.coefficient), height=round(100 * self.coefficient))
        GButton_181["command"] = self.GButton_181_command

        interval = Image.open(resource_path("img/text/interval.png"))
        interval = interval.resize((round(300 * self.coefficient), round(100 * self.coefficient)))
        intervalphoto = ImageTk.PhotoImage(interval)

        GButton_257 = tk.Button(self.root)
        GButton_257['bd'] = 0
        GButton_257["bg"] = "#f0f0f0"
        GButton_257["fg"] = "#000000"
        GButton_257["justify"] = "center"
        GButton_257["image"] = intervalphoto
        GButton_257.place(x=round(520 * self.coefficient), y=round(200 * self.coefficient), width=round(300 * self.coefficient), height=round(100 * self.coefficient))
        GButton_257["command"] = self.GButton_257_command

        keysignature = Image.open(resource_path("img/text/keysignature.png"))
        keysignature = keysignature.resize((round(300 * self.coefficient), round(100 * self.coefficient)))
        keysignaturephoto = ImageTk.PhotoImage(keysignature)

        GButton_348 = tk.Button(self.root)
        GButton_348['bd'] = 0
        GButton_348["bg"] = "#f0f0f0"
        GButton_348["fg"] = "#000000"
        GButton_348["justify"] = "center"
        GButton_348["image"] = keysignaturephoto
        GButton_348.place(x=round(140 * self.coefficient), y=round(380 * self.coefficient), width=round(300 * self.coefficient), height=round(100 * self.coefficient))
        GButton_348["command"] = self.GButton_348_command

        chord = Image.open(resource_path("img/text/chord.png"))
        chord = chord.resize((round(300 * self.coefficient), round(100 * self.coefficient)))
        chordphoto = ImageTk.PhotoImage(chord)

        GButton_987 = tk.Button(self.root)
        GButton_987['bd'] = 0
        GButton_987["bg"] = "#f0f0f0"
        GButton_987["fg"] = "#000000"
        GButton_987["justify"] = "center"
        GButton_987["image"] = chordphoto
        GButton_987.place(x=round(520 * self.coefficient), y=round(380 * self.coefficient), width=round(300 * self.coefficient), height=round(100 * self.coefficient))
        GButton_987["command"] = self.GButton_987_command

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
        Switch to Selection screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.selection import Selection
        s = Selection(self.root)

    def GButton_181_command(self):
        """
        Switch to Note screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.notation_exercises.note import Note
        n = Note(self.root)

    def GButton_257_command(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.notation_exercises.interval import Interval
        i = Interval(self.root)

    def GButton_348_command(self):
        """
        Switch to Key signature screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.notation_exercises.key_signature import Key_signature
        k = Key_signature(self.root)

    def GButton_987_command(self):
        """
        Switch to Chord screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.notation_exercises.chords import Chord
        c = Chord(self.root)
