from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import requests
import json
from PIL import Image, ImageTk


class ProductcheckoutGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1240x600")
        self.master.configure(bg="#FFFFFF")
        self.data = requests.get("http://127.0.0.1:8000/build")
        self.build = self.data.json()

        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path("./")

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
        self.canvas.create_rectangle(
            0.0,
            0.0,
            200.0,
            600.0,
            fill="#3653E9",
            outline=""
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets1("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=26.0,
            y=509.0,
            width=148.0,
            height=64.0
        )
           

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets1("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=1067.0,
            y=509.0,
            width=148.0,
            height=64.0
        )

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets1("image_1.png"))
        self.image_1 = self.canvas.create_image(
            100.0,
            78.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            237.0,
            19.0,
            anchor="nw",
            text="Checkout",
            fill="#000000",
            font=("Inter", 40 * -1)
        )
        
        if len(self.build) >= 1:
            img = Image.open(self.build[0]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_2 = ImageTk.PhotoImage(img)
            # self.image_image_2 = PhotoImage(
            #     file=self.relative_to_assets(self.build[0]['thumbnail_url']))
            self.image_2 = self.canvas.create_image(
                327.0,
                165.0,
                # width=350.0,
                # height =260.0,
                image=self.image_image_2)

            self.canvas.create_text(
                250.0,
                248.0,
                anchor="nw",
                text=self.build[0]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )

        if len(self.build) >= 2:
            img = Image.open(self.build[1]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_3 = ImageTk.PhotoImage(img)
            self.image_3 = self.canvas.create_image(
                514.0,
                165.0,
                image=self.image_image_3
            )

            self.canvas.create_text(
                444.0,
                248.0,
                anchor="nw",
                text=self.build[1]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        if len(self.build) >= 3:
            img = Image.open(self.build[2]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_4 = ImageTk.PhotoImage(img)
            self.image_4 = self.canvas.create_image(
                721.0,
                165.0,
                image=self.image_image_4
            )
            self.canvas.create_text(
                647.0,
                248.0,
                anchor="nw",
                text=self.build[2]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        if len(self.build) >= 4:    
            img = Image.open(self.build[3]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_5 = ImageTk.PhotoImage(img)
            self.image_5 = self.canvas.create_image(
                918.0,
                165.0,
                image=self.image_image_5
            )
            self.canvas.create_text(
                837.0,
                248.0,
                anchor="nw",
                text=self.build[3]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        if len(self.build) >= 5:   
            img = Image.open(self.build[4]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_6 = ImageTk.PhotoImage(img)
            self.image_6 = self.canvas.create_image(
                1115.0,
                165.0,
                image=self.image_image_6
            )
            self.canvas.create_text(
                1034.0,
                248.0,
                anchor="nw",
                text=self.build[4]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        if len(self.build) >= 6:    
            img = Image.open(self.build[5]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_7 = ImageTk.PhotoImage(img)
            self.image_7 = self.canvas.create_image(
                327.0,
                369.0,
                image=self.image_image_7
            )
            self.canvas.create_text(
                244.0,
                452.0,
                anchor="nw",
                text=self.build[5]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        if len(self.build) >= 7:    
            img = Image.open(self.build[6]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_8 = ImageTk.PhotoImage(img)
            self.image_8 = self.canvas.create_image(
                514.0,
                369.0,
                image=self.image_image_8
            )
            self.canvas.create_text(
                435.0,
                452.0,
                anchor="nw",
                text=self.build[6]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        if len(self.build) >= 8:
            img = Image.open(self.build[7]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_9 = ImageTk.PhotoImage(img)
            self.image_9 = self.canvas.create_image(
                721.0,
                369.0,
                image=self.image_image_9
            )
            self.canvas.create_text(
                641.0,
                452.0,
                anchor="nw",
                text=self.build[7]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        if len(self.build) >= 9:    
            img = Image.open(self.build[8]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_10 = ImageTk.PhotoImage(img)
            self.image_10 = self.canvas.create_image(
                918.0,
                369.0,
                image=self.image_image_10
            )
            self.canvas.create_text(
                837.0,
                451.0,
                anchor="nw",
                text=self.build[8]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        if len(self.build) >= 10:
            img = Image.open(self.build[9]['thumbnail_url'])
            img = img.resize((138, 138), Image.ANTIALIAS)
            self.image_image_11 = ImageTk.PhotoImage(img)
            self.image_11 = self.canvas.create_image(
                327.0,
                369.0,
                image=self.image_image_11
            )
            self.canvas.create_text(
                1026.0,
                451.0,
                anchor="nw",
                text=self.build[9]['full_name'],
                fill="#000000",
                font=("Inter SemiBold", 12 * -1)
            )
        url = "http://localhost:8000/build/price"
        response = requests.get(url)
        price = json.loads(response.text)
        self.canvas.create_text(
            257.0,
            521.0,
            anchor="nw",
            text="price : " + str(price['price']) + " baht",
            fill="#000000",
            font=("Inter SemiBold", 24 * -1)
        )
        self.master.resizable(False, False)
        self.master.mainloop()
        
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

    def relative_to_assets1(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def relative_to_assets(self, path: str) -> Path:
        return Path(path)
    
root = tk.Tk()
app = ProductcheckoutGUI(root)
root.mainloop()
