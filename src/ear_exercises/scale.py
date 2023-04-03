import tkinter as tk
from PIL import Image, ImageTk
import random
from src.dict.res_dict import resolution_dictionary
from src.dict.scale_dict import scale_dictionary
import json
import pygame
from vendor.rp import resource_path


class Scale:
    def __init__(self, root):
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height/540
        pygame.init()

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['scale_ear'][0]}/{self.stats['scale_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=round(3 * self.coefficient), width=round(150 * self.coefficient), height=round(20 * self.coefficient))

        self.scale = random.choice(tuple(scale_dictionary.keys()))
        self.sound = resource_path(random.choice(tuple(scale_dictionary[self.scale])))

        play_note = Image.open(resource_path('img/text/play_note.png'))
        play_note = play_note.resize((round(436 * self.coefficient), round(200 * self.coefficient)))
        self.play_notephoto = ImageTk.PhotoImage(play_note)

        self.play_button = tk.Button(self.root, command=self.play_audio)
        self.play_button.place(x=round(262 * self.coefficient), y=round(30 * self.coefficient), width=round(436 * self.coefficient), height=round(200 * self.coefficient))
        self.play_button['bd'] = 0
        self.play_button['image'] = self.play_notephoto

        major = Image.open(resource_path('img/text/scales/major.png'))
        major = major.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.majorphoto = ImageTk.PhotoImage(major)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.majorphoto
        GButton_554.place(x=round(245 * self.coefficient), y=round(280 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('major')

        minor = Image.open(resource_path('img/text/scales/minor.png'))
        minor = minor.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.minorphoto = ImageTk.PhotoImage(minor)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.minorphoto
        GButton_554.place(x=round(405 * self.coefficient), y=round(280 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('minor')

        hminor = Image.open(resource_path('img/text/scales/hminor.png'))
        hminor = hminor.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.hminorphoto = ImageTk.PhotoImage(hminor)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.hminorphoto
        GButton_554.place(x=round(565 * self.coefficient), y=round(280 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('hminor')

        mminor = Image.open(resource_path('img/text/scales/mminor.png'))
        mminor = mminor.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.mminorphoto = ImageTk.PhotoImage(mminor)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.mminorphoto
        GButton_554.place(x=round(245 * self.coefficient), y=round(365 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('mminor')

        dorian = Image.open(resource_path('img/text/scales/dorian.png'))
        dorian = dorian.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.dorianphoto = ImageTk.PhotoImage(dorian)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.dorianphoto
        GButton_554.place(x=round(405 * self.coefficient), y=round(365 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('dorian')

        phrygian = Image.open(resource_path('img/text/scales/phrygian.png'))
        phrygian = phrygian.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.phrygianphoto = ImageTk.PhotoImage(phrygian)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.phrygianphoto
        GButton_554.place(x=round(565 * self.coefficient), y=round(365 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('phrygian')

        lydian = Image.open(resource_path('img/text/scales/lydian.png'))
        lydian = lydian.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.lydianphoto = ImageTk.PhotoImage(lydian)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.lydianphoto
        GButton_554.place(x=round(245 * self.coefficient), y=round(450 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('lydian')

        mixolydian = Image.open(resource_path('img/text/scales/mixolydian.png'))
        mixolydian = mixolydian.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.mixolydianphoto = ImageTk.PhotoImage(mixolydian)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.mixolydianphoto
        GButton_554.place(x=round(405 * self.coefficient), y=round(450 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('mixolydian')

        locrian = Image.open(resource_path('img/text/scales/locrian.png'))
        locrian = locrian.resize((round(150 * self.coefficient), round(75 * self.coefficient)))
        self.locrianphoto = ImageTk.PhotoImage(locrian)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.locrianphoto
        GButton_554.place(x=round(565 * self.coefficient), y=round(450 * self.coefficient), width=round(150 * self.coefficient), height=round(75 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('locrian')

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
            self.stats["scale_ear"][1] += 1
            st.write(json.dumps(self.stats))
        if letter == self.scale:
            self.scale = random.choice(tuple(scale_dictionary.keys()))
            self.sound = resource_path(random.choice(tuple(scale_dictionary[self.scale])))

            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.correctphoto
            Label.place(x=round(415 * self.coefficient), y=round(240 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            with open(resource_path("profile/account.json"), 'w') as st:
                self.stats["scale_ear"][0] += 1
                st.write(json.dumps(self.stats))

            self.root.after(1000, lambda: Label.destroy())
            self.root.after(100, lambda: self.play_audio())
        else:
            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.incorrectphoto
            Label.place(x=round(415 * self.coefficient), y=round(240 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self.root.after(1000, lambda: Label.destroy())
        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['scale_ear'][0]}/{self.stats['scale_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=round(3 * self.coefficient), width=round(150 * self.coefficient), height=round(20 * self.coefficient))

    def play_audio(self):
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()

