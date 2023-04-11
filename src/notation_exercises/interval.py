import tkinter as tk
from PIL import Image, ImageTk
import random
from src.dict.interval_dict import interval_dictionary
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path
import json


class Interval:
    def __init__(self, root):
        """
        Interval
        :param root:
        """
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height/540

        self.interval = random.choice(tuple(interval_dictionary.keys()))
        intervalpath = random.choice(interval_dictionary[self.interval])

        intervalimg = Image.open(resource_path(intervalpath))
        intervalimg = intervalimg.resize((round(500 * self.coefficient), round(250 * self.coefficient)))
        self.intervalphoto = ImageTk.PhotoImage(intervalimg)

        self.GLabel_25 = tk.Label(self.root)
        self.GLabel_25["justify"] = "center"
        self.GLabel_25["image"] = self.intervalphoto
        self.GLabel_25['borderwidth'] = 2
        self.GLabel_25['relief'] = 'solid'
        self.GLabel_25.place(x=round(230 * self.coefficient), y=round(30 * self.coefficient), width=round(500 * self.coefficient), height=round(250 * self.coefficient))

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['interval_note'][0]}/{self.stats['interval_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=round(5 * self.coefficient), width=round(150 * self.coefficient), height=round(20 * self.coefficient))

        aug2 = Image.open(resource_path('img/intervals/buttons/aug2.png'))
        aug2 = aug2.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.aug2photo = ImageTk.PhotoImage(aug2)

        GButton_554 = tk.Button(self.root, bd=0, justify='center', image=self.aug2photo)
        GButton_554.place(x=round(270 * self.coefficient), y=round(320 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('aug2')

        aug3 = Image.open(resource_path('img/intervals/buttons/aug3.png'))
        aug3 = aug3.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.aug3photo = ImageTk.PhotoImage(aug3)

        GButton_897 = tk.Button(self.root, bd=0, justify='center', image=self.aug3photo)
        GButton_897.place(x=round(330 * self.coefficient), y=round(320 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GButton_897["command"] = lambda: self.submit('aug3')

        aug4 = Image.open(resource_path('img/intervals/buttons/aug4.png'))
        aug4 = aug4.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.aug4photo = ImageTk.PhotoImage(aug4)

        GButton_617 = tk.Button(self.root, bd=0, justify='center', image=self.aug4photo)
        GButton_617.place(x=round(390 * self.coefficient), y=round(320 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GButton_617["command"] = lambda: self.submit('aug4')

        aug5 = Image.open(resource_path('img/intervals/buttons/aug5.png'))
        aug5 = aug5.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.aug5photo = ImageTk.PhotoImage(aug5)

        GButton_285 = tk.Button(self.root, bd=0, justify='center', image=self.aug5photo)
        GButton_285.place(x=round(450 * self.coefficient), y=round(320 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GButton_285["command"] = lambda: self.submit('aug5')

        aug6 = Image.open(resource_path('img/intervals/buttons/aug6.png'))
        aug6 = aug6.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.aug6photo = ImageTk.PhotoImage(aug6)

        GButton_814 = tk.Button(self.root, bd=0, justify='center', image=self.aug6photo)
        GButton_814.place(x=round(510 * self.coefficient), y=round(320 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GButton_814["command"] = lambda: self.submit('aug6')

        aug7 = Image.open(resource_path('img/intervals/buttons/aug7.png'))
        aug7 = aug7.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.aug7photo = ImageTk.PhotoImage(aug7)

        GButton_579 = tk.Button(self.root, bd=0, justify='center', image=self.aug7photo)
        GButton_579.place(x=round(570 * self.coefficient), y=round(320 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GButton_579["command"] = lambda: self.submit('aug7')

        aug8 = Image.open(resource_path('img/intervals/buttons/aug8.png'))
        aug8 = aug8.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.aug8photo = ImageTk.PhotoImage(aug8)

        GButton_480 = tk.Button(self.root, bd=0, justify='center', image=self.aug8photo)
        GButton_480.place(x=round(630 * self.coefficient), y=round(320 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GButton_480["command"] = lambda: self.submit('aug8')

        maj2 = Image.open(resource_path('img/intervals/buttons/maj2.png'))
        maj2 = maj2.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.maj2photo = ImageTk.PhotoImage(maj2)

        GGGButton_554 = tk.Button(self.root, bd=0, justify='center', image=self.maj2photo)
        GGGButton_554.place(x=round(270 * self.coefficient), y=round(375 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGButton_554["command"] = lambda: self.submit('maj2')

        maj3 = Image.open(resource_path('img/intervals/buttons/maj3.png'))
        maj3 = maj3.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.maj3photo = ImageTk.PhotoImage(maj3)

        GGGButton_897 = tk.Button(self.root, bd=0, justify='center', image=self.maj3photo)
        GGGButton_897.place(x=round(330 * self.coefficient), y=round(375 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGButton_897["command"] = lambda: self.submit('maj3')

        p4 = Image.open(resource_path('img/intervals/buttons/p4.png'))
        p4 = p4.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.p4photo = ImageTk.PhotoImage(p4)

        GGGButton_617 = tk.Button(self.root, bd=0, justify='center', image=self.p4photo)
        GGGButton_617.place(x=round(390 * self.coefficient), y=round(375 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGButton_617["command"] = lambda: self.submit('p4')

        p5 = Image.open(resource_path('img/intervals/buttons/p5.png'))
        p5 = p5.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.p5photo = ImageTk.PhotoImage(p5)

        GGGButton_285 = tk.Button(self.root)
        GGGButton_285['bd'] = 0
        GGGButton_285["justify"] = "center"
        GGGButton_285["image"] = self.p5photo
        GGGButton_285.place(x=round(450 * self.coefficient), y=round(375 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGButton_285["command"] = lambda: self.submit('p5')

        maj6 = Image.open(resource_path('img/intervals/buttons/maj6.png'))
        maj6 = maj6.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.maj6photo = ImageTk.PhotoImage(maj6)

        GGGButton_814 = tk.Button(self.root)
        GGGButton_814['bd'] = 0
        GGGButton_814["justify"] = "center"
        GGGButton_814["image"] = self.maj6photo
        GGGButton_814.place(x=round(510 * self.coefficient), y=round(375 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGButton_814["command"] = lambda: self.submit('maj6')

        maj7 = Image.open(resource_path('img/intervals/buttons/maj7.png'))
        maj7 = maj7.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.maj7photo = ImageTk.PhotoImage(maj7)

        GGGButton_579 = tk.Button(self.root)
        GGGButton_579['bd'] = 0
        GGGButton_579["justify"] = "center"
        GGGButton_579["image"] = self.maj7photo
        GGGButton_579.place(x=round(570 * self.coefficient), y=round(375 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGButton_579["command"] = lambda: self.submit('maj7')

        p8 = Image.open(resource_path('img/intervals/buttons/p8.png'))
        p8 = p8.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.p8photo = ImageTk.PhotoImage(p8)

        GGGButton_480 = tk.Button(self.root)
        GGGButton_480['bd'] = 0
        GGGButton_480["justify"] = "center"
        GGGButton_480["image"] = self.p8photo
        GGGButton_480.place(x=round(630 * self.coefficient), y=round(375 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGButton_480["command"] = lambda: self.submit('p8')

        min2 = Image.open(resource_path('img/intervals/buttons/min2.png'))
        min2 = min2.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.min2photo = ImageTk.PhotoImage(min2)

        GGGGButton_554 = tk.Button(self.root)
        GGGGButton_554['bd'] = 0
        GGGGButton_554["justify"] = "center"
        GGGGButton_554["image"] = self.min2photo
        GGGGButton_554.place(x=round(270 * self.coefficient), y=round(430 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGGButton_554["command"] = lambda: self.submit('min2')

        min3 = Image.open(resource_path('img/intervals/buttons/min3.png'))
        min3 = min3.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.min3photo = ImageTk.PhotoImage(min3)

        GGGGButton_897 = tk.Button(self.root)
        GGGGButton_897['bd'] = 0
        GGGGButton_897["justify"] = "center"
        GGGGButton_897["image"] = self.min3photo
        GGGGButton_897.place(x=round(330 * self.coefficient), y=round(430 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGGButton_897["command"] = lambda: self.submit('min3')

        min6 = Image.open(resource_path('img/intervals/buttons/min6.png'))
        min6 = min6.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.min6photo = ImageTk.PhotoImage(min6)

        GGGGButton_814 = tk.Button(self.root)
        GGGGButton_814['bd'] = 0
        GGGGButton_814["justify"] = "center"
        GGGGButton_814["image"] = self.min6photo
        GGGGButton_814.place(x=round(510 * self.coefficient), y=round(430 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGGButton_814["command"] = lambda: self.submit('min6')

        min7 = Image.open(resource_path('img/intervals/buttons/min7.png'))
        min7 = min7.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.min7photo = ImageTk.PhotoImage(min7)

        GGGGButton_579 = tk.Button(self.root)
        GGGGButton_579['bd'] = 0
        GGGGButton_579["justify"] = "center"
        GGGGButton_579["image"] = self.min7photo
        GGGGButton_579.place(x=round(570 * self.coefficient), y=round(430 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGGGButton_579["command"] = lambda: self.submit('min7')

        dim2 = Image.open(resource_path('img/intervals/buttons/dim2.png'))
        dim2 = dim2.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.dim2photo = ImageTk.PhotoImage(dim2)

        GGButton_554 = tk.Button(self.root)
        GGButton_554['bd'] = 0
        GGButton_554["justify"] = "center"
        GGButton_554["image"] = self.dim2photo
        GGButton_554.place(x=round(270 * self.coefficient), y=round(485 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGButton_554["command"] = lambda: self.submit('dim2')

        dim3 = Image.open(resource_path('img/intervals/buttons/dim3.png'))
        dim3 = dim3.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.dim3photo = ImageTk.PhotoImage(dim3)

        GGButton_897 = tk.Button(self.root)
        GGButton_897['bd'] = 0
        GGButton_897["justify"] = "center"
        GGButton_897["image"] = self.dim3photo
        GGButton_897.place(x=round(330 * self.coefficient), y=round(485 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGButton_897["command"] = lambda: self.submit('dim3')

        dim4 = Image.open(resource_path('img/intervals/buttons/dim4.png'))
        dim4 = dim4.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.dim4photo = ImageTk.PhotoImage(dim4)

        GGButton_617 = tk.Button(self.root)
        GGButton_617['bd'] = 0
        GGButton_617["justify"] = "center"
        GGButton_617["image"] = self.dim4photo
        GGButton_617.place(x=round(390 * self.coefficient), y=round(485 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGButton_617["command"] = lambda: self.submit('dim4')

        dim5 = Image.open(resource_path('img/intervals/buttons/dim5.png'))
        dim5 = dim5.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.dim5photo = ImageTk.PhotoImage(dim5)

        GGButton_285 = tk.Button(self.root)
        GGButton_285['bd'] = 0
        GGButton_285["justify"] = "center"
        GGButton_285["image"] = self.dim5photo
        GGButton_285.place(x=round(450 * self.coefficient), y=round(485 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGButton_285["command"] = lambda: self.submit('dim5')

        dim6 = Image.open(resource_path('img/intervals/buttons/dim6.png'))
        dim6 = dim6.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.dim6photo = ImageTk.PhotoImage(dim6)

        GGButton_814 = tk.Button(self.root)
        GGButton_814['bd'] = 0
        GGButton_814["justify"] = "center"
        GGButton_814["image"] = self.dim6photo
        GGButton_814.place(x=round(510 * self.coefficient), y=round(485 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGButton_814["command"] = lambda: self.submit('dim6')

        dim7 = Image.open(resource_path('img/intervals/buttons/dim7.png'))
        dim7 = dim7.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.dim7photo = ImageTk.PhotoImage(dim7)

        GGButton_579 = tk.Button(self.root)
        GGButton_579['bd'] = 0
        GGButton_579["justify"] = "center"
        GGButton_579["image"] = self.dim7photo
        GGButton_579.place(x=round(570 * self.coefficient), y=round(485 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGButton_579["command"] = lambda: self.submit('dim7')

        dim8 = Image.open(resource_path('img/intervals/buttons/dim8.png'))
        dim8 = dim8.resize((round(45 * self.coefficient), round(45 * self.coefficient)))
        self.dim8photo = ImageTk.PhotoImage(dim8)

        GGButton_480 = tk.Button(self.root)
        GGButton_480['bd'] = 0
        GGButton_480["justify"] = "center"
        GGButton_480["image"] = self.dim8photo
        GGButton_480.place(x=round(630 * self.coefficient), y=round(485 * self.coefficient), width=round(45 * self.coefficient), height=round(45 * self.coefficient))
        GGButton_480["command"] = lambda: self.submit('dim8')

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
        GButton_172["justify"] = "center"
        GButton_172["image"] = arrowphoto
        GButton_172.place(x=round(30 * self.coefficient), y=round(5 * self.coefficient), width=round(122 * self.coefficient), height=round(122 * self.coefficient))
        GButton_172["command"] = self.GButton_172_command

        self.root.mainloop()

    def GButton_172_command(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.notation import Notation
        n = Notation(self.root)

    def submit(self, intrv: str):
        with open(resource_path("profile/account.json"), 'w') as st:
            self.stats["interval_note"][1] += 1
            st.write(json.dumps(self.stats))
        if intrv == self.interval:
            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.correctphoto
            Label.place(x=round(415 * self.coefficient), y=round(285 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self.interval = random.choice(tuple(interval_dictionary.keys()))
            intervalpath = resource_path(random.choice(interval_dictionary[self.interval]))

            self.GLabel_25.destroy()

            intervalimg = Image.open(intervalpath)
            intervalimg = intervalimg.resize((round(500 * self.coefficient), round(250 * self.coefficient)))
            self.intervalphoto = ImageTk.PhotoImage(intervalimg)

            self.GLabel_25 = tk.Label(self.root)
            self.GLabel_25["justify"] = "center"
            self.GLabel_25["image"] = self.intervalphoto
            self.GLabel_25['borderwidth'] = 2
            self.GLabel_25['relief'] = 'solid'
            self.GLabel_25.place(x=round(230 * self.coefficient), y=round(30 * self.coefficient), width=round(500 * self.coefficient), height=round(250 * self.coefficient))

            with open(resource_path("profile/account.json"), 'w') as st:
                self.stats["interval_note"][0] += 1
                st.write(json.dumps(self.stats))

            self.root.after(1000, lambda: Label.destroy())

        else:
            Label = tk.Label(self.root)
            Label["justify"] = "center"
            Label['image'] = self.incorrectphoto
            Label.place(x=round(415 * self.coefficient), y=round(285 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self.root.after(1000, lambda: Label.destroy())

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['interval_note'][0]}/{self.stats['interval_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=round(5 * self.coefficient), width=round(150 * self.coefficient), height=round(20 * self.coefficient))
