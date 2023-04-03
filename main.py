import json
from ctypes import windll

from src.app import App
from src.settings import Settings
import tkinter as tk
from PIL import Image, ImageTk
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path


def main(st: bool):
    with open(resource_path('settings/settings.json')) as settings:
        data = json.loads(settings.read())

    root = tk.Tk()

    im = Image.open(resource_path("img/icon.ico"))
    photo = ImageTk.PhotoImage(im)
    root.iconphoto(True, photo)
    root.title('Theorite')
    width = resolution_dictionary[data["resolution"]][0]
    height = resolution_dictionary[data["resolution"]][1]
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    match(data["resolution"]):
        case "fullscreen":
            root.attributes('-fullscreen', True)
        case "960":
            root.attributes('-fullscreen', False)
        case "zoomed":
            root.attributes('-fullscreen', False)
            root.state('zoomed')


    if not st:
        app = App(root)
    if st:
        app = Settings(root)


if __name__ == "__main__":
    main(False)
