from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

class OOPSpecGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("OOP Spec")
        self.master.geometry("1240x600")
        self.master.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            master,
            bg="#FFFFFF",
            height=600,
            width=1240,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            0.0,
            0.0,
            200.0,
            600.0,
            fill="#3653E9",
            outline="")

        self.canvas.create_text(
            239.0,
            30.0,
            anchor="nw",
            text="Payment Method",
            fill="#000000",
            font=("Inter", 40 * -1)
        )

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./assets/frame0")
        
        def relative_to_assets(path: str) -> Path:
            return self.ASSETS_PATH / Path(path)
        
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            100.0,
            101.0,
            image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=25.0,
            y=519.0,
            width=148.0,
            height=64.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=405.0,
            y=200.0,
            width=448.0,
            height=75.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=405.0,
            y=300.0,
            width=448.0,
            height=75.0
        )

        
        self.master.resizable(False, False)



root = Tk()
app = OOPSpecGUI(root)
root.mainloop()
