import tkinter as tk
from PIL import Image, ImageTk
import random
from src.dict.ear_note_dict import ear_note_dictionary
import json
import pygame
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path


class Note:
    def __init__(self, root):
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height/540
        pygame.init()

        self.note = random.choice(tuple(ear_note_dictionary.keys()))
        self.sound = resource_path(random.choice(tuple(ear_note_dictionary[self.note])))

        play_note = Image.open(resource_path('img/text/play_note.png'))
        play_note = play_note.resize((round(447 * self.coefficient), round(205 * self.coefficient)))
        self.play_notephoto = ImageTk.PhotoImage(play_note)

        self.play_button = tk.Button(self.root, command=self.play_audio)
        self.play_button.place(x=round(255 * self.coefficient), y=round(30 * self.coefficient), width=round(447 * self.coefficient), height=round(205 * self.coefficient))
        self.play_button['bd'] = 0
        self.play_button['image'] = self.play_notephoto

        middlec = Image.open(resource_path('img/text/middlec.png'))
        middlec = middlec.resize((round(180 * self.coefficient), round(180 * self.coefficient)))
        self.middlecphoto = ImageTk.PhotoImage(middlec)

        self.middlec_button = tk.Button(self.root, command=self.play_middlec)
        if self.data["middle_c"]:
            self.middlec_button.place(x=round(750 * self.coefficient), y=round(42 * self.coefficient), width=round(180 * self.coefficient), height=round(180 * self.coefficient))
        self.middlec_button['bd'] = 0
        self.middlec_button['image'] = self.middlecphoto

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['note_ear'][0]}/{self.stats['note_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=round(3 * self.coefficient), width=round(150 * self.coefficient), height=round(20 * self.coefficient))

        C = Image.open(resource_path('img/text/C.png'))
        C = C.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.cphoto = ImageTk.PhotoImage(C)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.cphoto
        GButton_554.place(x=round(275 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('C')

        Cs = Image.open(resource_path('img/text/csharp.png'))
        if self.data['european_notation']:
            Cs = Image.open(resource_path('img/text/cis.png'))
        Cs = Cs.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.csphoto = ImageTk.PhotoImage(Cs)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.csphoto
        GButton_554.place(x=round(275 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('Cis')

        D = Image.open(resource_path('img/text/D.png'))
        D = D.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.dphoto = ImageTk.PhotoImage(D)

        GButton_897 = tk.Button(self.root)
        GButton_897["bg"] = "#f0f0f0"
        GButton_897["fg"] = "#000000"
        GButton_897['bd'] = 0
        GButton_897["justify"] = "center"
        GButton_897["image"] = self.dphoto
        GButton_897.place(x=round(335 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_897["command"] = lambda: self.submit('D')

        Dis = Image.open(resource_path('img/text/dsharp.png'))
        if self.data['european_notation']:
            Dis = Image.open(resource_path('img/text/dis.png'))
        Dis = Dis.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.dsphoto = ImageTk.PhotoImage(Dis)

        GButton_897 = tk.Button(self.root)
        GButton_897["bg"] = "#f0f0f0"
        GButton_897["fg"] = "#000000"
        GButton_897['bd'] = 0
        GButton_897["justify"] = "center"
        GButton_897["image"] = self.dsphoto
        GButton_897.place(x=round(335 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_897["command"] = lambda: self.submit('Dis')

        E = Image.open(resource_path('img/text/E.png'))
        E = E.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.ephoto = ImageTk.PhotoImage(E)

        GButton_617 = tk.Button(self.root)
        GButton_617["bg"] = "#f0f0f0"
        GButton_617["fg"] = "#000000"
        GButton_617['bd'] = 0
        GButton_617["justify"] = "center"
        GButton_617["image"] = self.ephoto
        GButton_617.place(x=round(395 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
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
        GButton_285.place(x=round(455 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_285["command"] = lambda: self.submit('F')

        Fis = Image.open(resource_path('img/text/fsharp.png'))
        if self.data['european_notation']:
            Fis = Image.open(resource_path('img/text/fis.png'))
        Fis = Fis.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.fisphoto = ImageTk.PhotoImage(Fis)

        GButton_285 = tk.Button(self.root)
        GButton_285["bg"] = "#f0f0f0"
        GButton_285["fg"] = "#000000"
        GButton_285['bd'] = 0
        GButton_285["justify"] = "center"
        GButton_285["image"] = self.fisphoto
        GButton_285.place(x=round(455 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_285["command"] = lambda: self.submit('Fis')

        G = Image.open(resource_path('img/text/G.png'))
        G = G.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.gphoto = ImageTk.PhotoImage(G)

        GButton_814 = tk.Button(self.root)
        GButton_814["bg"] = "#f0f0f0"
        GButton_814['bd'] = 0
        GButton_814["fg"] = "#000000"
        GButton_814["justify"] = "center"
        GButton_814["image"] = self.gphoto
        GButton_814.place(x=round(515 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_814["command"] = lambda: self.submit('G')

        Gis = Image.open(resource_path('img/text/gsharp.png'))
        if self.data['european_notation']:
            Gis = Image.open(resource_path('img/text/gis.png'))
        Gis = Gis.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.gisphoto = ImageTk.PhotoImage(Gis)

        GButton_814 = tk.Button(self.root)
        GButton_814["bg"] = "#f0f0f0"
        GButton_814['bd'] = 0
        GButton_814["fg"] = "#000000"
        GButton_814["justify"] = "center"
        GButton_814["image"] = self.gisphoto
        GButton_814.place(x=round(515 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_814["command"] = lambda: self.submit('Gis')

        A = Image.open(resource_path('img/text/A.png'))
        A = A.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.aphoto = ImageTk.PhotoImage(A)

        GButton_579 = tk.Button(self.root)
        GButton_579["bg"] = "#f0f0f0"
        GButton_579["fg"] = "#000000"
        GButton_579['bd'] = 0
        GButton_579["justify"] = "center"
        GButton_579["image"] = self.aphoto
        GButton_579.place(x=round(575 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_579["command"] = lambda: self.submit('A')

        Ais = Image.open(resource_path('img/text/asharp.png'))
        if self.data['european_notation']:
            Ais = Image.open(resource_path('img/text/b.png'))
        Ais = Ais.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.aisphoto = ImageTk.PhotoImage(Ais)

        GButton_579 = tk.Button(self.root)
        GButton_579["bg"] = "#f0f0f0"
        GButton_579["fg"] = "#000000"
        GButton_579['bd'] = 0
        GButton_579["justify"] = "center"
        GButton_579["image"] = self.aisphoto
        GButton_579.place(x=round(575 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_579["command"] = lambda: self.submit('Ais')

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
        GButton_480.place(x=round(635 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_480["command"] = lambda: self.submit('B')

        correct = Image.open(resource_path('img/text/correct.png'))
        correct = correct.resize((round(108 * self.coefficient), round(30 * self.coefficient)))
        self.correctphoto = ImageTk.PhotoImage(correct)

        incorrect = Image.open(resource_path('img/text/incorrect.png'))
        incorrect = incorrect.resize((round(129 * self.coefficient), round(30 * self.coefficient)))
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
        pygame.quit()
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.ear import Ear
        e = Ear(self.root)

    def submit(self, letter: str):
        with open(resource_path("profile/account.json"), 'w') as st:
            self.stats["note_ear"][1] += 1
            st.write(json.dumps(self.stats))
        if letter == self.note:
            self.note = random.choice(tuple(ear_note_dictionary.keys()))
            self.sound = resource_path(random.choice(tuple(ear_note_dictionary[self.note])))

            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.correctphoto
            Label.place(x=round(415 * self.coefficient), y=round(270 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            with open(resource_path("profile/account.json"), 'w') as st:
                self.stats["note_ear"][0] += 1
                st.write(json.dumps(self.stats))

            self.root.after(1000, lambda: Label.destroy())
            self.root.after(100, lambda: self.play_audio())
        else:
            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.incorrectphoto
            Label.place(x=round(415 * self.coefficient), y=round(270 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self.root.after(1000, lambda: Label.destroy())

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['note_ear'][0]}/{self.stats['note_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=round(3 * self.coefficient), width=round(150 * self.coefficient), height=round(20 * self.coefficient))

    def play_audio(self):
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()

    def play_middlec(self):
        pygame.mixer.music.load(resource_path('sounds/notes/c3.flac'))
        pygame.mixer.music.play()
