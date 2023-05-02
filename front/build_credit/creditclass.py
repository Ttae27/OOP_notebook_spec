from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class PaymentDetailForm:
    def __init__(self, master):
        self.master = master

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

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=1060.0, y=499.0, width=148.0, height=64.0)
        
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_waytopay(),
            relief="flat"
        )
        self.button_2.place(
            x=25.0,
            y=519.0,
            width=148.0,
            height=64.0
        )
        
        self.canvas.create_rectangle(
            0.0,
            0.0,
            458.0,
            600.0,
            fill="#3653E9",
            outline=""
        )

        self.canvas.create_text(
            565.0,
            50.0,
            anchor="nw",
            text="Payment detail",
            fill="#000000",
            font=("Inter", 40 * -1)
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            758.5,
            301.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=570.0, y=274.0, width=377.0, height=52.0)

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            611.5,
            393.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(x=570.0, y=366.0, width=83.0, height=52.0)

        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            722.5,
            393.0,
            image=self.entry_image_3
        )
        self.entry_3 =Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(x=681.0, y=366.0, width=83.0, height=52.0)

        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            865.5,
            393.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(x=824.0, y=366.0, width=83.0, height=52.0)

        self.entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            758.5,
            196.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(x=570.0, y=169.0, width=377.0, height=52.0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            197.0,
            273.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            565.0,
            140.0,
            anchor="nw",
            text="Card holder name:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            565.0,
            245.0,
            anchor="nw",
            text="Card number:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            819.0,
            337.0,
            anchor="nw",
            text="CVV:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            565.0,
            337.0,
            anchor="nw",
            text="EXP date: dd/mm",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.master.resizable(False, False)
        self.master.mainloop()


if __name__ == "__main__":
    window = Tk()
    payment_form = PaymentDetailForm(window)