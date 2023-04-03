import tkinter as tk
from PIL import Image, ImageTk
import random
from src.dict.ear_interval_dict import ear_interval_dictionary
import json
import pygame
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path


class Interval:
    def __init__(self, root):
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height/540
        pygame.init()

        self.interval = random.choice(tuple(ear_interval_dictionary.keys()))
        self.sound = resource_path(random.choice(tuple(ear_interval_dictionary[self.interval])))

        play_note = Image.open(resource_path('img/text/play_note.png'))
        play_note = play_note.resize((round(447 * self.coefficient), round(205 * self.coefficient)))
        self.play_notephoto = ImageTk.PhotoImage(play_note)

        self.play_button = tk.Button(self.root, command=self.play_audio)
        self.play_button.place(x=round(255 * self.coefficient), y=round(20 * self.coefficient), width=round(447 * self.coefficient), height=round(205 * self.coefficient))
        self.play_button['bd'] = 0
        self.play_button['image'] = self.play_notephoto

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['interval_ear'][0]}/{self.stats['interval_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=0, width=round(150 * self.coefficient), height=round(20 * self.coefficient))

        minor2 = Image.open(resource_path('img/text/ear_intervals/minor2.png'))
        minor2 = minor2.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.minor2cphoto = ImageTk.PhotoImage(minor2)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.minor2cphoto
        GButton_554.place(x=round(320 * self.coefficient), y=round(240 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('minor2')

        major2 = Image.open(resource_path('img/text/ear_intervals/major2.png'))
        major2 = major2.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.major2cphoto = ImageTk.PhotoImage(major2)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.major2cphoto
        GButton_554.place(x=round(430 * self.coefficient), y=round(240 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('major2')

        minor3 = Image.open(resource_path('img/text/ear_intervals/minor3.png'))
        minor3 = minor3.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.minor3cphoto = ImageTk.PhotoImage(minor3)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.minor3cphoto
        GButton_554.place(x=round(540 * self.coefficient), y=round(240 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('minor3')

        major3 = Image.open(resource_path('img/text/ear_intervals/major3.png'))
        major3 = major3.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.major3cphoto = ImageTk.PhotoImage(major3)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.major3cphoto
        GButton_554.place(x=round(320 * self.coefficient), y=round(300 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('major3')

        fourth = Image.open(resource_path('img/text/ear_intervals/4.png'))
        fourth = fourth.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.fourthcphoto = ImageTk.PhotoImage(fourth)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.fourthcphoto
        GButton_554.place(x=round(430 * self.coefficient), y=round(300 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('4')

        tritone = Image.open(resource_path('img/text/ear_intervals/tritone.png'))
        tritone = tritone.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.tritonecphoto = ImageTk.PhotoImage(tritone)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.tritonecphoto
        GButton_554.place(x=round(540 * self.coefficient), y=round(300 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('tritone')

        fifth = Image.open(resource_path('img/text/ear_intervals/5.png'))
        fifth = fifth.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.fifthcphoto = ImageTk.PhotoImage(fifth)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.fifthcphoto
        GButton_554.place(x=round(320 * self.coefficient), y=round(360 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('5')

        minor6 = Image.open(resource_path('img/text/ear_intervals/minor6.png'))
        minor6 = minor6.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.minor6cphoto = ImageTk.PhotoImage(minor6)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.minor6cphoto
        GButton_554.place(x=round(430 * self.coefficient), y=round(360 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('minor6')

        major6 = Image.open(resource_path('img/text/ear_intervals/major6.png'))
        major6 = major6.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.major6cphoto = ImageTk.PhotoImage(major6)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.major6cphoto
        GButton_554.place(x=round(540 * self.coefficient), y=round(360 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('major6')

        minor7 = Image.open(resource_path('img/text/ear_intervals/minor7.png'))
        minor7 = minor7.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.minor7cphoto = ImageTk.PhotoImage(minor7)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.minor7cphoto
        GButton_554.place(x=round(320 * self.coefficient), y=round(420 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('minor7')

        major7 = Image.open(resource_path('img/text/ear_intervals/major7.png'))
        major7 = major7.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.major7cphoto = ImageTk.PhotoImage(major7)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.major7cphoto
        GButton_554.place(x=round(430 * self.coefficient), y=round(420 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('major7')

        octave = Image.open(resource_path('img/text/ear_intervals/8.png'))
        octave = octave.resize((round(100 * self.coefficient), round(50 * self.coefficient)))
        self.octavecphoto = ImageTk.PhotoImage(octave)

        GButton_554 = tk.Button(self.root)
        GButton_554["bg"] = "#f0f0f0"
        GButton_554["fg"] = "#000000"
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.octavecphoto
        GButton_554.place(x=round(540 * self.coefficient), y=round(420 * self.coefficient), width=round(100 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('8')

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
            self.stats["interval_ear"][1] += 1
            st.write(json.dumps(self.stats))
        if letter == self.interval:
            self.interval = random.choice(tuple(ear_interval_dictionary.keys()))
            self.sound = resource_path(random.choice(tuple(ear_interval_dictionary[self.interval])))

            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.correctphoto
            Label.place(x=round(415 * self.coefficient), y=round(490 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            with open(resource_path("profile/account.json"), 'w') as st:
                self.stats["interval_ear"][0] += 1
                st.write(json.dumps(self.stats))

            self.root.after(1000, lambda: Label.destroy())
            self.root.after(100, lambda: self.play_audio())
        else:
            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.incorrectphoto
            Label.place(x=round(415 * self.coefficient), y=round(490 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self.root.after(1000, lambda: Label.destroy())

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['interval_ear'][0]}/{self.stats['interval_ear'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=0, width=round(150 * self.coefficient), height=round(20 * self.coefficient))

    def play_audio(self):
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()
