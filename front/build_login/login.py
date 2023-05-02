from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class LoginUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1240x600")
        self.master.configure(bg="#FFFFFF")
        
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./assets/frame0")
        
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
        
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(293.0, 425.0, image=self.image_image_1)
        
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.master,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=912.8680419921875, y=519.8560180664062, width=228.1319580078125, height=39.14398193359375)
        
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.master,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )
        self.button_2.place(x=807.0, y=429.0, width=169.0, height=46.40189743041992)
        
        self.canvas.create_text(794.0, 30.0, anchor="nw", text="OOP SPEC", fill="#000000", font=("Inter SemiBold", 48 * -1))
        
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(904.5, 361.5, image=self.entry_image_1)
        self.entry_1 = Entry(
            self.master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter SemiBold", 20 * -1),
            highlightthickness=0
        )
        self.entry_1.place(x=707.0, y=332.0, width=395.0, height=57.0)
        
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(904.5, 196.5, image=self.entry_image_2)
        self.entry_2 = Entry(
            self.master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter SemiBold", 20 * -1),
            # padx=10,
            # pady=10,
            highlightthickness=0
        )
        self.entry_2.place(x=707.0, y=167.0 ,width=395.0,height=57.0)
        self.canvas.create_text(707.0, 295.0, anchor="nw", text="Password", fill="#000000", font=("Inter SemiBold", 20 * -1))
        
        self.canvas.create_text(707.0, 125.0, anchor="nw", text="Username", fill="#000000", font=("Inter SemiBold", 20 * -1))
        
        self.canvas.create_text(647.0, 528.0, anchor="nw", text="Don’t have an account?", fill="#000000", font=("Inter SemiBold", 20 * -1))
        
        self.master.resizable(False, False)
        self.master.mainloop()
        
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def login(self):
        name = self.entry_2.get()
        password = self.entry_1.get()
        print(name)
        print(password)

if __name__ == "__main__":
    window = Tk()
    app = LoginUI(window)
