from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class PaymentDetail:
    
    def __init__(self, master):
        self.__master = master
        self.__master.geometry("1240x600")
        self.__master.configure(bg = "#FFFFFF")
        
        self.canvas = Canvas(
            self.__master,
            bg = "#FFFFFF",
            height = 600,
            width = 1240,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        
        self.canvas.create_rectangle(
            0.0,
            0.0,
            458.0,
            600.0,
            fill="#3653E9",
            outline="")
        
        self.canvas.create_text(
            527.0,
            37.0,
            anchor="nw",
            text="Payment detail",
            fill="#000000",
            font=("Inter", 40 * -1)
        )
        
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./build_qr/assets/frame0")
        
        def relative_to_assets(path: str) -> Path:
            return self.ASSETS_PATH / Path(path)
        
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            229.0,
            299.0,
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
            x=1061.0,
            y=511.0,
            width=148.0,
            height=64.0
        )
        
        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            808.0,
            314.0,
            image=self.image_image_2
        )
        
        self.__master.resizable(False, False)
        self.__master.mainloop()

root = Tk()
app = PaymentDetail(root)
