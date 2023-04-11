import tkinter as tk
from PIL import Image, ImageTk
import random
from src.dict.key_signature_dict import key_signature_dictionary, modes
import json
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path


class Key_signature:
    def __init__(self, root):
        """
        Key signature window object
        :param root: tkinter window object
        """
        with open(resource_path('settings/settings.json')) as settings:
            self.data = json.loads(settings.read())
        with open(resource_path('profile/account.json')) as statistics:
            self.stats = json.loads(statistics.read())

        self.root = root

        height = resolution_dictionary[self.data["resolution"]][1]
        self.coefficient = height/540

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['key_note'][0]}/{self.stats['key_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=0,
                             width=round(150 * self.coefficient), height=round(20 * self.coefficient))

        self._key_signature_pic_path = random.choice(list(key_signature_dictionary.keys()))
        self.possible_key_signatures = key_signature_dictionary[self._key_signature_pic_path]

        ksimg = Image.open(resource_path(self._key_signature_pic_path))
        ksimg = ksimg.resize((round(500 * self.coefficient), round(189 * self.coefficient)))
        self.ksphoto = ImageTk.PhotoImage(ksimg)

        self.GLabel_25 = tk.Label(self.root, justify='center', image=self.ksphoto, borderwidth=2, relief='solid')
        self.GLabel_25.place(x=round(230 * self.coefficient), y=round(20 * self.coefficient),
                             width=round(500 * self.coefficient), height=round(189 * self.coefficient))

        self.random_mode = random.choice(tuple(modes.keys()))
        if not self.data["modes"]:
            self.random_mode = random.choice((tuple(modes.keys())[0], tuple(modes.keys())[1]))
        self.mode = self.random_mode[0]
        self.mode_dimensions = self.random_mode[1]

        md = Image.open(resource_path(self.mode))
        md = md.resize(self.mode_dimensions)
        self.mdphoto = ImageTk.PhotoImage(md)

        x = (round(960 * self.coefficient) - self.mode_dimensions[0]) / 2

        self.GLabel_25 = tk.Label(self.root, justify='center', image=self.mdphoto)
        self.GLabel_25.place(x=x, y=round(210 * self.coefficient),
                             width=self.mode_dimensions[0], height=self.mode_dimensions[1])

        Cb = Image.open(resource_path('img/text/Cb.png'))
        if self.data["european_notation"]:
            Cb = Image.open(resource_path('img/text/ces.png'))
        Cb = Cb.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.cbphoto = ImageTk.PhotoImage(Cb)

        GButton_554 = tk.Button(self.root, bd=0, justify='center', image=self.cbphoto)
        GButton_554.place(x=round(270 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('Cb', modes[self.random_mode])

        Db = Image.open(resource_path('img/text/Db.png'))
        if self.data["european_notation"]:
            Db = Image.open(resource_path('img/text/des.png'))
        Db = Db.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.dbphoto = ImageTk.PhotoImage(Db)

        GButton_897 = tk.Button(self.root, bd=0, justify='center', image=self.dbphoto)
        GButton_897.place(x=round(330 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_897["command"] = lambda: self.submit('Db', modes[self.random_mode])

        Eb = Image.open(resource_path('img/text/Eb.png'))
        if self.data["european_notation"]:
            Eb = Image.open(resource_path('img/text/es.png'))
        Eb = Eb.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.ebphoto = ImageTk.PhotoImage(Eb)

        GButton_617 = tk.Button(self.root, bd=0, justify='center', image=self.ebphoto)
        GButton_617.place(x=round(390 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_617["command"] = lambda: self.submit('Eb', modes[self.random_mode])

        Fb = Image.open(resource_path('img/text/Fb.png'))
        if self.data["european_notation"]:
            Fb = Image.open(resource_path('img/text/fes.png'))
        Fb = Fb.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.fbphoto = ImageTk.PhotoImage(Fb)

        GButton_285 = tk.Button(self.root)
        GButton_285['bd'] = 0
        GButton_285["justify"] = "center"
        GButton_285["image"] = self.fbphoto
        GButton_285.place(x=round(450 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_285["command"] = lambda: self.submit('Fb', modes[self.random_mode])

        Gb = Image.open(resource_path('img/text/Gb.png'))
        if self.data["european_notation"]:
            Gb = Image.open(resource_path('img/text/ges.png'))
        Gb = Gb.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.gbphoto = ImageTk.PhotoImage(Gb)

        GButton_814 = tk.Button(self.root)
        GButton_814['bd'] = 0
        GButton_814["justify"] = "center"
        GButton_814["image"] = self.gbphoto
        GButton_814.place(x=round(510 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_814["command"] = lambda: self.submit('Gb', modes[self.random_mode])

        Ab = Image.open(resource_path('img/text/Ab.png'))
        if self.data["european_notation"]:
            Ab = Image.open(resource_path('img/text/as.png'))
        Ab = Ab.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.abphoto = ImageTk.PhotoImage(Ab)

        GButton_579 = tk.Button(self.root)
        GButton_579['bd'] = 0
        GButton_579["justify"] = "center"
        GButton_579["image"] = self.abphoto
        GButton_579.place(x=round(570 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_579["command"] = lambda: self.submit('Ab', modes[self.random_mode])

        Bb = Image.open(resource_path('img/text/Bb.png'))
        if self.data['european_notation']:
            Bb = Image.open(resource_path('img/text/B.png'))
        Bb = Bb.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.bbphoto = ImageTk.PhotoImage(Bb)

        GButton_480 = tk.Button(self.root)
        GButton_480['bd'] = 0
        GButton_480["justify"] = "center"
        GButton_480["image"] = self.bbphoto
        GButton_480.place(x=round(630 * self.coefficient), y=round(320 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_480["command"] = lambda: self.submit('Bb', modes[self.random_mode])

        C = Image.open(resource_path('img/text/C.png'))
        C = C.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.cphoto = ImageTk.PhotoImage(C)

        GButton_554 = tk.Button(self.root, bd=0, justify='center', image=self.cphoto)
        GButton_554.place(x=round(270 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('C', modes[self.random_mode])

        D = Image.open(resource_path('img/text/D.png'))
        D = D.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.dphoto = ImageTk.PhotoImage(D)

        GButton_897 = tk.Button(self.root, bd=0, justify='center', image=self.dphoto)
        GButton_897.place(x=round(330 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_897["command"] = lambda: self.submit('D', modes[self.random_mode])

        E = Image.open(resource_path('img/text/E.png'))
        E = E.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.ephoto = ImageTk.PhotoImage(E)

        GButton_617 = tk.Button(self.root, bd=0, justify='center', image=self.ephoto)
        GButton_617.place(x=round(390 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_617["command"] = lambda: self.submit('E', modes[self.random_mode])

        F = Image.open(resource_path('img/text/F.png'))
        F = F.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.fphoto = ImageTk.PhotoImage(F)

        GButton_285 = tk.Button(self.root, bd=0, justify='center', image=self.fphoto)
        GButton_285.place(x=round(450 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_285["command"] = lambda: self.submit('F', modes[self.random_mode])

        G = Image.open(resource_path('img/text/G.png'))
        G = G.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.gphoto = ImageTk.PhotoImage(G)

        GButton_814 = tk.Button(self.root, bd=0, justify='center', image=self.gphoto)
        GButton_814.place(x=round(510 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_814["command"] = lambda: self.submit('G', modes[self.random_mode])

        A = Image.open(resource_path('img/text/A.png'))
        A = A.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.aphoto = ImageTk.PhotoImage(A)

        GButton_579 = tk.Button(self.root, bd=0, justify='center', image=self.aphoto)
        GButton_579.place(x=round(570 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_579["command"] = lambda: self.submit('A', modes[self.random_mode])

        B = Image.open(resource_path('img/text/B.png'))
        if self.data['european_notation']:
            B = Image.open(resource_path('img/text/H.png'))
        B = B.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.bphoto = ImageTk.PhotoImage(B)

        GButton_480 = tk.Button(self.root, bd=0, justify='center', image=self.bphoto)
        GButton_480.place(x=round(630 * self.coefficient), y=round(380 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_480["command"] = lambda: self.submit('B', modes[self.random_mode])

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

        Cs = Image.open(resource_path('img/text/csharp.png'))
        if self.data["european_notation"]:
            Cs = Image.open(resource_path('img/text/cis.png'))
        Cs = Cs.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.csphoto = ImageTk.PhotoImage(Cs)

        GButton_554 = tk.Button(self.root)
        GButton_554['bd'] = 0
        GButton_554["justify"] = "center"
        GButton_554["image"] = self.csphoto
        GButton_554.place(x=round(270 * self.coefficient), y=round(440 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_554["command"] = lambda: self.submit('C#', modes[self.random_mode])

        Ds = Image.open(resource_path('img/text/dsharp.png'))
        if self.data["european_notation"]:
            Ds = Image.open(resource_path('img/text/dis.png'))
        Ds = Ds.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.dsphoto = ImageTk.PhotoImage(Ds)

        GButton_897 = tk.Button(self.root)
        GButton_897['bd'] = 0
        GButton_897["justify"] = "center"
        GButton_897["image"] = self.dsphoto
        GButton_897.place(x=round(330 * self.coefficient), y=round(440 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_897["command"] = lambda: self.submit('D#', modes[self.random_mode])

        Es = Image.open(resource_path('img/text/esharp.png'))
        if self.data["european_notation"]:
            Es = Image.open(resource_path('img/text/eis.png'))
        Es = Es.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.esphoto = ImageTk.PhotoImage(Es)

        GButton_617 = tk.Button(self.root)
        GButton_617['bd'] = 0
        GButton_617["justify"] = "center"
        GButton_617["image"] = self.esphoto
        GButton_617.place(x=round(390 * self.coefficient), y=round(440 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_617["command"] = lambda: self.submit('E#', modes[self.random_mode])

        Fs = Image.open(resource_path('img/text/fsharp.png'))
        if self.data["european_notation"]:
            Fs = Image.open(resource_path('img/text/fis.png'))
        Fs = Fs.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.fsphoto = ImageTk.PhotoImage(Fs)

        GButton_285 = tk.Button(self.root)
        GButton_285['bd'] = 0
        GButton_285["justify"] = "center"
        GButton_285["image"] = self.fsphoto
        GButton_285.place(x=round(450 * self.coefficient), y=round(440 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_285["command"] = lambda: self.submit('F#', modes[self.random_mode])

        Gs = Image.open(resource_path('img/text/gsharp.png'))
        if self.data["european_notation"]:
            Gs = Image.open(resource_path('img/text/gis.png'))
        Gs = Gs.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.gsphoto = ImageTk.PhotoImage(Gs)

        GButton_814 = tk.Button(self.root)
        GButton_814['bd'] = 0
        GButton_814["justify"] = "center"
        GButton_814["image"] = self.gsphoto
        GButton_814.place(x=round(510 * self.coefficient), y=round(440 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_814["command"] = lambda: self.submit('G#', modes[self.random_mode])

        As = Image.open(resource_path('img/text/asharp.png'))
        if self.data["european_notation"]:
            As = Image.open(resource_path('img/text/ais.png'))
        As = As.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.asphoto = ImageTk.PhotoImage(As)

        GButton_579 = tk.Button(self.root)
        GButton_579['bd'] = 0
        GButton_579["justify"] = "center"
        GButton_579["image"] = self.asphoto
        GButton_579.place(x=round(570 * self.coefficient), y=round(440 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_579["command"] = lambda: self.submit('A#', modes[self.random_mode])

        Bs = Image.open(resource_path('img/text/bsharp.png'))
        if self.data['european_notation']:
            Bs = Image.open(resource_path('img/text/his.png'))
        Bs = Bs.resize((round(50 * self.coefficient), round(50 * self.coefficient)))
        self.bsphoto = ImageTk.PhotoImage(Bs)

        GButton_480 = tk.Button(self.root)
        GButton_480['bd'] = 0
        GButton_480["justify"] = "center"
        GButton_480["image"] = self.bsphoto
        GButton_480.place(x=round(630 * self.coefficient), y=round(440 * self.coefficient), width=round(50 * self.coefficient), height=round(50 * self.coefficient))
        GButton_480["command"] = lambda: self.submit('B#', modes[self.random_mode])

        self.root.mainloop()

    def GButton_172_command(self):
        """
        Switch to Notation screen
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        from src.notation import Notation
        n = Notation(self.root)

    def submit(self, letter: str, mde: str):
        """
        Submit answer for evaluation
        :param letter: Note clicked by user
        :param mde: Mode displayed on screen
        """
        with open(resource_path("profile/account.json"), 'w') as st:
            self.stats["key_note"][1] += 1
            st.write(json.dumps(self.stats))

        if ' '.join((letter, mde)) in self.possible_key_signatures:
            Label = tk.Label(self.root, justify='center', image=self.correctphoto)
            Label.place(x=round(415 * self.coefficient), y=round(500 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self._key_signature_pic_path = random.choice(list(key_signature_dictionary.keys()))
            self.possible_key_signatures = key_signature_dictionary[self._key_signature_pic_path]

            ksimg = Image.open(resource_path(self._key_signature_pic_path))
            ksimg = ksimg.resize((round(500 * self.coefficient), round(189 * self.coefficient)))
            self.ksphoto = ImageTk.PhotoImage(ksimg)

            self.GLabel_25 = tk.Label(self.root, justify='center', image=self.ksphoto, borderwidth=2, relief='solid')
            self.GLabel_25.place(x=round(230 * self.coefficient), y=round(20 * self.coefficient), width=round(500 * self.coefficient), height=round(189 * self.coefficient))

            self.random_mode = random.choice(tuple(modes.keys()))
            if not self.data["modes"]:
                self.random_mode = random.choice((tuple(modes.keys())[0], tuple(modes.keys())[1]))
            self.mode = self.random_mode[0]
            self.mode_dimensions = self.random_mode[1]

            md = Image.open(resource_path(self.mode))
            md = md.resize(self.mode_dimensions)
            self.mdphoto = ImageTk.PhotoImage(md)

            x = (round(960 * self.coefficient) - self.mode_dimensions[0]) / 2

            self.GLabel_25 = tk.Label(self.root, justify='center', image=self.mdphoto)
            self.GLabel_25.place(x=x, y=round(210 * self.coefficient), width=self.mode_dimensions[0], height=self.mode_dimensions[1])

            with open(resource_path("profile/account.json"), 'w') as st:
                self.stats["key_note"][0] += 1
                st.write(json.dumps(self.stats))

            self.root.after(1000, lambda: Label.destroy())

        else:
            Label = tk.Label(self.root, justify='center', image=self.incorrectphoto)
            Label.place(x=round(415 * self.coefficient), y=round(500 * self.coefficient), width=round(129 * self.coefficient), height=round(30 * self.coefficient))

            self.root.after(1000, lambda: Label.destroy())

        self.GLabel_27 = tk.Label(self.root)
        self.GLabel_27["justify"] = "center"
        self.GLabel_27["text"] = str(f"{self.stats['key_note'][0]}/{self.stats['key_note'][1]}")
        self.GLabel_27['borderwidth'] = 0
        self.GLabel_27['relief'] = 'solid'
        self.GLabel_27.place(x=round(405 * self.coefficient), y=0, width=round(150 * self.coefficient), height=round(20 * self.coefficient))
