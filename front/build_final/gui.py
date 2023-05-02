from tkinter import *
from pathlib import Path

class PaymentSuccessful:
    def __init__(self, master):
        self.master = master
        self.master.title("Payment Successful")
        self.master.geometry("1240x600")
        self.master.configure(bg="#3653E9")
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\LENOVO\Desktop\build\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return self.ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self.master,
            bg="#3653E9",
            height=600,
            width=1240,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_text(
            364.0,
            192.0,
            anchor="nw",
            text="Payment Successful",
            fill="#FFFFFF",
            font=("Inter", 64 * -1)
        )

        self.canvas.create_text(
            385.0,
            305.0,
            anchor="nw",
            text="Thank you for your kind support",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_rectangle(
            382.0,
            299.0,
            992.0,
            300.0,
            fill="#FFFFFF",
            outline=""
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            293.0,
             260.0,
             image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=1058.0,
            y=505.0,
            width=148.0,
            height=64.0
        )
        self.master.resizable(False, False)
        self.master.mainloop()

# Example usage:
root = Tk()
app = PaymentSuccessful(root)
root.mainloop()