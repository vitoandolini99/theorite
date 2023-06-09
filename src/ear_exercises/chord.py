import tkinter as tk
from PIL import Image, ImageTk
import random
from src.dict.ear_chord_dict import chord_dictionary
import json
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path
import pygame


class Chord:
    def __init__(self, root):
        """
        Chord window object
        :param root: tkinter window object
        """
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height/540
        pygame.init()

        self.chord = random.choice(tuple(chord_dictionary.keys()))
        self.sound = resource_path(random.choice(tuple(chord_dictionary[self.chord])))

        play_note = Image.open(resource_path('img/text/play_note.png'))
        play_note = play_note.resize((round(447 * self.coefficient), round(205 * self.coefficient)))
        self.play_notephoto = ImageTk.PhotoImage(play_note)

        self.play_button = tk.Button(self.root, command=self.play_audio)
        self.play_button.place(x=round(255 * self.coefficient), y=round(20 * self.coefficient), width=round(447 * self.coefficient), height=round(205 * self.coefficient))
        self.play_button['bd'] = 0
        self.play_button['image'] = self.play_notephoto

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['chord_ear'][0]}/{self.stats['chord_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=0, width=round(150 * self.coefficient), height=round(20 * self.coefficient))

        major = Image.open(resource_path('img/text/major.png'))
        major = major.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.majorphoto = ImageTk.PhotoImage(major)

        minor = Image.open(resource_path('img/text/minor.png'))
        minor = minor.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.minorphoto = ImageTk.PhotoImage(minor)

        augtriad = Image.open(resource_path('img/text/augtriad.png'))
        augtriad = augtriad.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.augtriadphoto = ImageTk.PhotoImage(augtriad)

        dimtriad = Image.open(resource_path('img/text/dimtriad.png'))
        dimtriad = dimtriad.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.dimtriadphoto = ImageTk.PhotoImage(dimtriad)

        dominant7 = Image.open(resource_path('img/text/dominant7.png'))
        dominant7 = dominant7.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.dominant7photo = ImageTk.PhotoImage(dominant7)

        major7 = Image.open(resource_path('img/text/major7.png'))
        major7 = major7.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.major7photo = ImageTk.PhotoImage(major7)

        minor7 = Image.open(resource_path('img/text/minor7.png'))
        minor7 = minor7.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.minor7photo = ImageTk.PhotoImage(minor7)

        minormajor7 = Image.open(resource_path('img/text/minormajor7.png'))
        minormajor7 = minormajor7.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.minormajor7photo = ImageTk.PhotoImage(minormajor7)

        halfdim7 = Image.open(resource_path('img/text/halfdim7.png'))
        halfdim7 = halfdim7.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.halfdim7photo = ImageTk.PhotoImage(halfdim7)

        dim7 = Image.open(resource_path('img/text/dim7.png'))
        dim7 = dim7.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.dim7photo = ImageTk.PhotoImage(dim7)

        aug7 = Image.open(resource_path('img/text/aug7.png'))
        aug7 = aug7.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.aug7photo = ImageTk.PhotoImage(aug7)

        augmajor7 = Image.open(resource_path('img/text/augmajor7.png'))
        augmajor7 = augmajor7.resize((round(125 * self.coefficient), round(45 * self.coefficient)))
        self.augmajor7photo = ImageTk.PhotoImage(augmajor7)

        sus2 = Image.open(resource_path('img/text/sus2.png'))
        sus2 = sus2.resize((round(170 * self.coefficient), round(45 * self.coefficient)))
        self.sus2photo = ImageTk.PhotoImage(sus2)

        sus4 = Image.open(resource_path('img/text/sus4.png'))
        sus4 = sus4.resize((round(170 * self.coefficient), round(45 * self.coefficient)))
        self.sus4photo = ImageTk.PhotoImage(sus4)

        dominant7sus4 = Image.open(resource_path('img/text/dominant7sus4.png'))
        dominant7sus4 = dominant7sus4.resize((round(170 * self.coefficient), round(45 * self.coefficient)))
        self.dominant7sus4photo = ImageTk.PhotoImage(dominant7sus4)

        GButton_178 = tk.Button(self.root, bd=0)
        GButton_178["justify"] = "center"
        GButton_178["image"] = self.majorphoto
        GButton_178.place(x=round(215 * self.coefficient), y=round(250 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_178["command"] = lambda: self.submit('major_triad')

        GButton_809 = tk.Button(self.root, bd=0)
        GButton_809["justify"] = "center"
        GButton_809["image"] = self.minorphoto
        GButton_809.place(x=round(350 * self.coefficient), y=round(250 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_809["command"] = lambda: self.submit('minor_triad')

        GButton_426 = tk.Button(self.root, bd=0)
        GButton_426["justify"] = "center"
        GButton_426["image"] = self.augtriadphoto
        GButton_426.place(x=round(485 * self.coefficient), y=round(250 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_426["command"] = lambda: self.submit('aug')

        GButton_922 = tk.Button(self.root, bd=0)
        GButton_922["justify"] = "center"
        GButton_922["image"] = self.dimtriadphoto
        GButton_922.place(x=round(620 * self.coefficient), y=round(250 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_922["command"] = lambda: self.submit('dim')

        GButton_178 = tk.Button(self.root, bd=0)
        GButton_178["justify"] = "center"
        GButton_178["image"] = self.dominant7photo
        GButton_178.place(x=round(215 * self.coefficient), y=round(305 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_178["command"] = lambda: self.submit('dom7')

        GButton_809 = tk.Button(self.root, bd=0)
        GButton_809["justify"] = "center"
        GButton_809["image"] = self.major7photo
        GButton_809.place(x=round(350 * self.coefficient), y=round(305 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_809["command"] = lambda: self.submit('major7')

        GButton_426 = tk.Button(self.root, bd=0)
        GButton_426["justify"] = "center"
        GButton_426["image"] = self.minor7photo
        GButton_426.place(x=round(485 * self.coefficient), y=round(305 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_426["command"] = lambda: self.submit('minor7')

        GButton_922 = tk.Button(self.root, bd=0)
        GButton_922["justify"] = "center"
        GButton_922["image"] = self.minormajor7photo
        GButton_922.place(x=round(620 * self.coefficient), y=round(305 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_922["command"] = lambda: self.submit('minormajor7')

        GButton_178 = tk.Button(self.root, bd=0)
        GButton_178["justify"] = "center"
        GButton_178["image"] = self.halfdim7photo
        GButton_178.place(x=round(215 * self.coefficient), y=round(360 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_178["command"] = lambda: self.submit('halfdim7')

        GButton_809 = tk.Button(self.root, bd=0)
        GButton_809["justify"] = "center"
        GButton_809["image"] = self.dim7photo
        GButton_809.place(x=round(350 * self.coefficient), y=round(360 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_809["command"] = lambda: self.submit('dim7')

        GButton_426 = tk.Button(self.root, bd=0)
        GButton_426["justify"] = "center"
        GButton_426["image"] = self.aug7photo
        GButton_426.place(x=round(485 * self.coefficient), y=round(360 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_426["command"] = lambda: self.submit('aug7')

        GButton_922 = tk.Button(self.root, bd=0)
        GButton_922["justify"] = "center"
        GButton_922["image"] = self.augmajor7photo
        GButton_922.place(x=round(620 * self.coefficient), y=round(360 * self.coefficient), width=round(125 * self.coefficient), height=round(45 * self.coefficient))
        GButton_922["command"] = lambda: self.submit('augmajor7')

        GButton_809 = tk.Button(self.root, bd=0)
        GButton_809["justify"] = "center"
        GButton_809["image"] = self.sus2photo
        GButton_809.place(x=round(215 * self.coefficient), y=round(415 * self.coefficient), width=round(170 * self.coefficient), height=round(45 * self.coefficient))
        GButton_809["command"] = lambda: self.submit('sus2')

        GButton_426 = tk.Button(self.root, bd=0)
        GButton_426["justify"] = "center"
        GButton_426["image"] = self.sus4photo
        GButton_426.place(x=round(395 * self.coefficient), y=round(415 * self.coefficient), width=round(170 * self.coefficient), height=round(45 * self.coefficient))
        GButton_426["command"] = lambda: self.submit('sus4')

        GButton_922 = tk.Button(self.root, bd=0)
        GButton_922["justify"] = "center"
        GButton_922["image"] = self.dominant7sus4photo
        GButton_922.place(x=round(575 * self.coefficient), y=round(415 * self.coefficient), width=round(170 * self.coefficient), height=round(45 * self.coefficient))
        GButton_922["command"] = lambda: self.submit('dom7sus4')

        correct = Image.open(resource_path('img/text/correct.png'))
        correct = correct.resize((round(108 * self.coefficient), round(30 * self.coefficient)))
        self.correctphoto = ImageTk.PhotoImage(correct)

        incorrect = Image.open(resource_path('img/text/incorrect.png'))
        incorrect = incorrect.resize((round(129 * self.coefficient), round(30 * self.coefficient)))
        self.incorrectphoto = ImageTk.PhotoImage(incorrect)

        arrow = Image.open(resource_path("img/back_arrow.png"))
        arrow = arrow.resize((round(122 * self.coefficient), round(122 * self.coefficient)))
        self.arrowphoto = ImageTk.PhotoImage(arrow)

        GButton_172 = tk.Button(self.root)
        GButton_172["bd"] = 0
        GButton_172["justify"] = "center"
        GButton_172["image"] = self.arrowphoto
        GButton_172.place(x=round(30 * self.coefficient), y=round(5 * self.coefficient), width=round(122 * self.coefficient), height=round(122 * self.coefficient))
        GButton_172["command"] = self.GButton_172_command

    def GButton_172_command(self):
        """
        Switch to Ear screen
        """
        pygame.quit()
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.ear import Ear
        e = Ear(self.root)

    def submit(self, letter: str):
        """
        Submit chord
        :param letter: Chord clicked
        """
        with open(resource_path("profile/account.json"), 'w') as st:
            self.stats["chord_ear"][1] += 1
            st.write(json.dumps(self.stats))

        if letter == self.chord:
            self.chord = random.choice(tuple(chord_dictionary.keys()))
            self.sound = resource_path(random.choice(tuple(chord_dictionary[self.chord])))

            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.correctphoto
            Label.place(x=round(415 * self.coefficient), y=round(480 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self.root.after(1000, lambda: Label.destroy())
            self.root.after(100, lambda: self.play_audio())

            with open(resource_path("profile/account.json"), 'w') as st:
                self.stats["chord_ear"][0] += 1
                st.write(json.dumps(self.stats))
        else:
            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.incorrectphoto
            Label.place(x=round(415 * self.coefficient), y=round(480 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self.root.after(1000, lambda: Label.destroy())

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['chord_ear'][0]}/{self.stats['chord_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=0, width=round(150 * self.coefficient), height=round(20 * self.coefficient))

    def play_audio(self):
        """
        Play audio button (plays current chord)
        """
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()
