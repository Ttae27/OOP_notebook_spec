
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer



# from tkinter import *
# Explicit imports to satisfy Flake8
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:/Users/ADMIN/Desktop/notonedrive/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1240x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1240,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    293.0,
    425.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1021.0,
    y=513.0,
    width=169.0,
    height=46.40189743041992
)

canvas.create_text(
    794.0,
    30.0,
    anchor="nw",
    text="OOP SPEC",
    fill="#000000",
    font=("Inter SemiBold", 48 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    754.5,
    187.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    padx= 10,
    pady= 10,
    font=("Inter SemiBold", 18 * -1),
    highlightthickness=0
)
entry_1.place(
    x=618.0,
    y=166.0,
    width=273.0,
    height=41.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1077.5,
    187.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    padx= 10,
    pady= 10,
    font=("Inter SemiBold", 18 * -1),
    highlightthickness=0
)
entry_2.place(
    x=941.0,
    y=166.0,
    width=273.0,
    height=41.0
)

canvas.create_text(
    951.0,
    125.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    629.0,
    125.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    772.0,
    425.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    padx= 10,
    pady= 10,
    font=("Inter SemiBold", 18 * -1),
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=618.0,
    y=404.0,
    width=308.0,
    height=41.0
)

canvas.create_text(
    629.0,
    359.0,
    anchor="nw",
    text="Phone",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    909.0,
    308.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    padx= 10,
    pady= 10,
    font=("Inter SemiBold", 18 * -1),
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=618.0,
    y=283.0,
    width=582.0,
    height=48.0
)

canvas.create_text(
    631.0,
    239.0,
    anchor="nw",
    text="Address",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
