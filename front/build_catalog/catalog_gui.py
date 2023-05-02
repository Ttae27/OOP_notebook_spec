from tkinter import *
from pathlib import Path

class MyApp:
    def __init__(self, master):
        self.master = master
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.master.geometry("1240x600")
        self.master.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=600,
            width=1240,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(100.0, 300.0, image=image_image_1)

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=1101.0, y=552.0, width=117.0, height=29.25)

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=23.0, y=531.0, width=130.0, height=36.0)

        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(x=0.0, y=473.0, width=200.0, height=30.0)

        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(x=0.0, y=438.0, width=200.0, height=30.0)

        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(x=0.0, y=403.0, width=200.0, height=30.0)

        button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(x=0.0, y=369.0, width=200.0, height=30.0)

        button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(x=0.0, y=333.0, width=200.0, height=30.0)

        button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(x=0.0, y=298.0, width=200.0, height=30.0)

        button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.button_9.place(x=0.0, y=263.0, width=200.0, height=30.0)

        button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(x=1.12994384765625, y=229.0, width=200.0, height=30.0)

        button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self.button_11.place(x=0.0, y=193.0, width=200.0, height=30.0)

        button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self.button_12.place(x=0.0, y=158.0, width=200.0, height=30.0)

        self.canvas.create_text(
            38.0,
            16.0,
            anchor="nw",
            text="OOP SPEC",
            fill="#FFFFFF",
            font=("Inter SemiBold", 24 * -1)
        )
        self.master.resizable(False, False)
        self.master.mainloop()

window = Tk()
app = MyApp(window)
