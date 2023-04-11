import tkinter as tk
from PIL import Image, ImageTk
import random
from src.dict.note_dict import note_dictionary
import json
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path


class Note:
    def __init__(self, root):
        """
        Note window object
        :param root: tkinter window object
        """
        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height / 540

        self.note = random.choice(("A", "B", "C", "D", "E", "F", "G"))
        notepath = random.choice(note_dictionary[self.note])

        noteimg = Image.open(resource_path(notepath))
        noteimg = noteimg.resize((round(500 * self.coefficient), round(250 * self.coefficient)))
        self.notephoto = ImageTk.PhotoImage(noteimg)

        self.GLabel_25 = tk.Label(self.root)
        self.GLabel_25["justify"] = "center"
        self.GLabel_25["image"] = self.notephoto
        self.GLabel_25['borderwidth'] = 2
        self.GLabel_25['relief'] = 'solid'
        self.GLabel_25.place(x=round(230 * self.coefficient), y=round(30 * self.coefficient), width=round(500 * self.coefficient), height=round(250 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['note_note'][0]}/{self.stats['note_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=round(5 * self.coefficient), width=round(150 * self.coefficient), height=round(20 * self.coefficient))

        C = Image.open(resource_path('img/text/C.png'))
        C = C.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.cphoto = ImageTk.PhotoImage(C)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.cphoto
        GButton_554.place(x=round(270 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('C')

        D = Image.open(resource_path('img/text/D.png'))
        D = D.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.dphoto = ImageTk.PhotoImage(D)

        GButton_897 = tk.Button(self.root)
        GButton_897["bg"] = "#f0f0f0"
        GButton_897["fg"] = "#000000"
        GButton_897['bd'] = 0
        GButton_897["justify"] = "center"
        GButton_897["image"] = self.dphoto
        GButton_897.place(x=round(330 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_897["command"] = lambda: self.submit('D')

        E = Image.open(resource_path('img/text/E.png'))
        E = E.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.ephoto = ImageTk.PhotoImage(E)

        GButton_617 = tk.Button(self.root)
        GButton_617["bg"] = "#f0f0f0"
        GButton_617["fg"] = "#000000"
        GButton_617['bd'] = 0
        GButton_617["justify"] = "center"
        GButton_617["image"] = self.ephoto
        GButton_617.place(x=round(390 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_617["command"] = lambda: self.submit('E')

        F = Image.open(resource_path('img/text/F.png'))
        F = F.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.fphoto = ImageTk.PhotoImage(F)

        GButton_285 = tk.Button(self.root)
        GButton_285["bg"] = "#f0f0f0"
        GButton_285["fg"] = "#000000"
        GButton_285['bd'] = 0
        GButton_285["justify"] = "center"
        GButton_285["image"] = self.fphoto
        GButton_285.place(x=round(450 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_285["command"] = lambda: self.submit('F')

        G = Image.open(resource_path('img/text/G.png'))
        G = G.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.gphoto = ImageTk.PhotoImage(G)

        GButton_814 = tk.Button(self.root)
        GButton_814["bg"] = "#f0f0f0"
        GButton_814['bd'] = 0
        GButton_814["fg"] = "#000000"
        GButton_814["justify"] = "center"
        GButton_814["image"] = self.gphoto
        GButton_814.place(x=round(510 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_814["command"] = lambda: self.submit('G')

        A = Image.open(resource_path('img/text/A.png'))
        A = A.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.aphoto = ImageTk.PhotoImage(A)

        GButton_579 = tk.Button(self.root)
        GButton_579["bg"] = "#f0f0f0"
        GButton_579["fg"] = "#000000"
        GButton_579['bd'] = 0
        GButton_579["justify"] = "center"
        GButton_579["image"] = self.aphoto
        GButton_579.place(x=round(570 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_579["command"] = lambda: self.submit('A')

        B = Image.open(resource_path('img/text/B.png'))
        if self.data['european_notation']:
            B = Image.open(resource_path('img/text/H.png'))
        B = B.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.bphoto = ImageTk.PhotoImage(B)

        GButton_480 = tk.Button(self.root)
        GButton_480["bg"] = "#f0f0f0"
        GButton_480['bd'] = 0
        GButton_480["fg"] = "#000000"
        GButton_480["justify"] = "center"
        GButton_480["image"] = self.bphoto
        GButton_480.place(x=round(630 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_480["command"] = lambda: self.submit('B')

        correct = Image.open(resource_path('img/text/correct.png'))
        correct = correct.resize((round(324 * self.coefficient), round(90 * self.coefficient)))
        self.correctphoto = ImageTk.PhotoImage(correct)

        incorrect = Image.open(resource_path('img/text/incorrect.png'))
        incorrect = incorrect.resize((round(387 * self.coefficient), round(90 * self.coefficient)))
        self.incorrectphoto = ImageTk.PhotoImage(incorrect)

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
        Switch to Notation screen=
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.notation import Notation
        n = Notation(self.root)

    def submit(self, letter: str):
        """
        Submit answer for evaluation
        :param letter: Note clicked by user
        """
        with open(resource_path("profile/account.json"), 'w') as st:
            self.stats["note_note"][1] += 1
            st.write(json.dumps(self.stats))

        if letter == self.note:
            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.correctphoto
            Label.place(x=round(286 * self.coefficient), y=round(420 * self.coefficient), width=round(387 * self.coefficient), height=round(90 * self.coefficient))

            self.note = random.choice(("A", "B", "C", "D", "E", "F", "G"))
            notepath = random.choice(note_dictionary[self.note])

            self.GLabel_25.destroy()

            noteimg = Image.open(resource_path(notepath))
            noteimg = noteimg.resize((round(500 * self.coefficient), round(250 * self.coefficient)))
            self.notephoto = ImageTk.PhotoImage(noteimg)

            self.GLabel_25 = tk.Label(self.root)
            self.GLabel_25["justify"] = "center"
            self.GLabel_25["image"] = self.notephoto
            self.GLabel_25['borderwidth'] = 2
            self.GLabel_25['relief'] = 'solid'
            self.GLabel_25.place(x=round(230 * self.coefficient), y=round(30 * self.coefficient), width=round(500 * self.coefficient), height=round(250 * self.coefficient))

            with open(resource_path("profile/account.json"), 'w') as st:
                self.stats["note_note"][0] += 1
                st.write(json.dumps(self.stats))

            self.root.after(1000, lambda: Label.destroy())
        else:
            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.incorrectphoto
            Label.place(x=round(286 * self.coefficient), y=round(420 * self.coefficient), width=round(387 * self.coefficient), height=round(90 * self.coefficient))

            self.root.after(1000, lambda: Label.destroy())

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['note_note'][0]}/{self.stats['note_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=round(5 * self.coefficient), width=round(150 * self.coefficient), height=round(20 * self.coefficient))
