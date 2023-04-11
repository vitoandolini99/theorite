import json
from src.app import App
from src.settings import Settings
import tkinter as tk
from PIL import Image, ImageTk
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path
from src.db.db_connection import mydb, mycursor
import uuid

mac_address = uuid.getnode()
mac_address_hex = ':'.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0, 8 * 6, 8)][::-1])


def ondelete():
    with open(resource_path('profile/account.json')) as statistics:
        st = json.dumps(statistics.read())

    with open(resource_path('settings/settings.json')) as settings:
        dt = json.dumps(settings.read())
    mycursor.execute(f"update Bomboclaat set stngs='{dt}', acc='{st}' where mac_addr='{mac_address_hex}';")
    mydb.commit()


def main(st: bool):
    if not st:
        with open(resource_path('profile/account.json'), 'r') as statistics:
            sct = json.dumps(statistics.read())

        with open(resource_path('settings/settings.json'), 'r') as settings:
            dt = json.dumps(settings.read())
        try:
            mycursor.execute(f"insert into bomboclaat(mac_addr, stngs, acc) values ('{mac_address_hex}', '{dt}', '{sct}');")
        except Exception:
            pass
        with open(resource_path('settings/settings.json'), 'w') as s:
            mycursor.execute(f"select stngs from bomboclaat where mac_addr='{mac_address_hex}';")
            s.write(str(mycursor.fetchone()).replace("""\\""", '')[3:-4])

        with open(resource_path('profile/account.json'), 'w') as scs:
            mycursor.execute(f"select acc from bomboclaat where mac_addr='{mac_address_hex}';")
            scs.write(str(mycursor.fetchone()).replace("""\\""", '')[3:-4])

        mydb.commit()
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

    match (data["resolution"]):
        case "fullscreen":
            root.attributes('-fullscreen', True)
        case "960":
            root.attributes('-fullscreen', False)
    if not st:
        app = App(root)
    if st:
        app = Settings(root)
    root.mainloop()

    try:
        root.protocol("WM_DELETE_WINDOW", ondelete())
    except tk.TclError:
        pass


if __name__ == "__main__":
    main(False)
