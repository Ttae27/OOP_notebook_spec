import tkinter as tk
from tkinter import ttk
import requests
import json
from tkinter import *
from urllib.parse import unquote
from PIL import Image, ImageTk
from tkinter import messagebox
import time
#convvert from figma to tkinter
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class HomePageGUI:
    def __init__(self, master):
        self.__master = master
        screen_width = self.__master.winfo_screenwidth()
        screen_height = self.__master.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        self.__master.geometry(f"{window_width}x{window_height}")
        master.title("Home Page")

        # Create sign in button
        self.__signin_button = tk.Button(master, text="Sign In", command=self.open_login)
        self.__signin_button.pack()

        # Create sign up button
        self.__signup_button = tk.Button(master, text="Sign Up", command=self.open_signup)
        self.__signup_button.pack()

    def open_login(self):
        self.__master.destroy()
        login_window = tk.Tk()
        login_gui = LoginGUI(login_window)
        login_window.mainloop()

    def open_signup(self):
        self.__master.destroy()
        signup_window = tk.Tk()
        signup_gui = SignupGUI(signup_window)
        signup_window.mainloop()



class LoginGUI:
    def __init__(self, master):
        self.__master = master
        self.__master.geometry("1240x600")
        self.__master.configure(bg="#FFFFFF")
        
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./build_login/assets/frame0")
        
        self.canvas = Canvas(
            self.__master,
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
            self.__master,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_signup,
            relief="flat"
        )
        self.button_1.place(x=912.8680419921875, y=519.8560180664062, width=228.1319580078125, height=39.14398193359375)
        
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.__master,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command= self.open_catalog ,
            relief="flat"
        )
        self.button_2.place(x=807.0, y=429.0, width=169.0, height=46.40189743041992)
        
        self.canvas.create_text(794.0, 30.0, anchor="nw", text="OOP SPEC", fill="#000000", font=("Inter SemiBold", 48 * -1))
        
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(904.5, 361.5, image=self.entry_image_1)
        self.__password_entry = Entry(
            self.__master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter SemiBold", 20 * -1),
            highlightthickness=0
        )
        self.__password_entry.place(x=707.0, y=332.0, width=395.0, height=57.0)
        
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(904.5, 196.5, image=self.entry_image_2)
        self.__username_entry = Entry(
            self.__master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter SemiBold", 20 * -1),
            highlightthickness=0
        )
        self.__username_entry.place(x=707.0, y=167.0 ,width=395.0,height=57.0)
        self.canvas.create_text(707.0, 295.0, anchor="nw", text="Password", fill="#000000", font=("Inter SemiBold", 20 * -1))
        
        self.canvas.create_text(707.0, 125.0, anchor="nw", text="Username", fill="#000000", font=("Inter SemiBold", 20 * -1))
        
        self.canvas.create_text(647.0, 528.0, anchor="nw", text="Don’t have an account?", fill="#000000", font=("Inter SemiBold", 20 * -1))
        
        self.__master.resizable(False, False)
        self.__master.mainloop()
        
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    

    def login(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()

        credential = {'username': username, 'password': password}
        response = requests.post('http://localhost:8000/signin', json=credential)
        data = response.json()
        print(username)
        print(password)
        # self.__status_label.config(text=f"{data}")
        return data
    
    def on_click(self):
        messagebox.showinfo("Status: ", "User does not exist. Do you want to sign up?")
            
    def open_catalog(self):
        # print(self.login_status_button)
        data = self.login()
        if data == {"Status": "User does not exist. Do you want to sign up?"}:
            self.on_click()
        if data == {"Status": "log in successfully"}:
            self.__master.destroy()
            catalog_window = tk.Tk()
            login_gui = ProductCatalogGUI(catalog_window)
            catalog_window.mainloop()
            
    def open_signup(self):
        self.__master.destroy()
        signup_window = tk.Tk()
        signup_gui = SignupGUI(signup_window)
        signup_window.mainloop()
            
class SignupGUI:
    def __init__(self, master):
        self.__master = master
        self.status = False
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./build_sign_up/assets/frame0")
        self.__master.geometry("1240x600")
        self.__master.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.__master,
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
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.condition,
            relief="flat"
        )
        self.button_1.place(x=1021.0, y=513.0, width=169.0, height=46.40189743041992)

        self.canvas.create_text(794.0, 30.0, anchor="nw", text="OOP SPEC", fill="#000000", font=("Inter SemiBold", 48 * -1))

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(754.5, 187.5, image=self.entry_image_1)
        self.__username_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter SemiBold", 18 * -1),
            highlightthickness=0
        )
        self.__username_entry.place(x=618.0, y=166.0, width=273.0, height=41.0)

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(1077.5, 187.5, image=self.entry_image_2)
        self.__password_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter SemiBold", 18 * -1),
            highlightthickness=0
        )
        self.__password_entry.place(x=941.0, y=166.0, width=273.0, height=41.0)

        self.canvas.create_text(951.0, 125.0, anchor="nw", text="Password", fill="#000000", font=("Inter SemiBold", 20 * -1))

        self.canvas.create_text(629.0, 125.0, anchor="nw", text="Username", fill="#000000", font=("Inter SemiBold", 20 * -1))

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(772.0, 425.5, image=self.entry_image_3)
        self.__phone_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            font=("Inter SemiBold", 18 * -1),
            fg="#000716",
            highlightthickness=0
        )
        self.__phone_entry.place(x=618.0, y=404.0, width=308.0, height=41.0)

        self.canvas.create_text(629.0, 359.0, anchor="nw", text="Phone", fill="#000000", font=("Inter SemiBold", 20 * -1))

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(909.0, 308.0, image=self.entry_image_4)
        self.__address_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            font=("Inter SemiBold", 18 * -1),
            fg="#000716",
            highlightthickness=0
        )
        self.__address_entry.place(x=618.0, y=283.0, width=582.0, height=48.0)

        self.canvas.create_text(631.0, 239.0, anchor="nw", text="Address", fill="#000000", font=("Inter SemiBold", 20 * -1))

        self.__master.resizable(False, False)
        self.__master.mainloop()
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def clear_text(self):
        self.__username_entry.delete(0,END)
        self.__password_entry.delete(0,END)
        self.__address_entry.delete(0,END)
        self.__phone_entry.delete(0,END)
        # .delete(0, END)
        
    def open_login(self):
        self.__master.destroy()
        catalog_window = tk.Tk()
        login_gui = LoginGUI(catalog_window)
        catalog_window.mainloop()

    def popup_status_error(self):
        messagebox.showinfo('Notify', 'This username has been used')
        
    def popup_status_completed(self):
        messagebox.showinfo('Notify', 'Successfully sign up')
        
    
    def signup(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()
        address = self.__address_entry.get()
        phone = self.__phone_entry.get()
        print()
        user_data = {'username': username, 'password': password, 'delivery_address': address, 'phone': phone}
        response = requests.post('http://localhost:8000/signup', json=user_data)
        data = response.json()
        return data
    
    def condition(self):
        data = self.signup()
        if data == {'Notify': 'Successfully sign up'}:
            self.popup_status_completed()
            self.open_login()
        elif data == {'Notify': 'This username has been used'}:
            self.popup_status_error()
            self.clear_text()
               
    @property
    def  username_entry(self):
        return  self.__username_entry
    
    @property
    def password_entry(self):
        return self.__password_entry
    
    @property
    def address_entry(self):
        return self.__address_entry
    
    @property
    def phone_entry(self):
        return self.__phone_entry

class ProductCatalogGUI:
    def __init__(self, master):
        self.__master = master
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./build_catalog/assets/frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.__master.geometry("1240x600")
        self.__master.configure(bg="#FFFFFF")
        self.__width = 200.0
        self.__height = 30.0
        self.__y = 120.0
        self.__x = 0

        self.canvas = Canvas(
            self.__master,
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
        self.canvas.create_text(
            38.0,
            16.0,
            anchor="nw",
            text="OOP SPEC",
            fill="#FFFFFF",
            font=("Inter SemiBold", 24 * -1)
        )
        # Create the catalog buttons 
        self.__catalogs = ["cpu", "gpu", "cooling", "hdd", "monitor", "motherboard", "pc_case", "psu", "ram", "ssd"]
        
        self.button_image = [] #load image for button
        for i in range(len(self.__catalogs)):
            self.button_image.append(
                PhotoImage(file=relative_to_assets("button_"+str(i+1)+".png")) #load image name form 3-12
            )
        
        self.button = []
        for i, catalog in enumerate(self.__catalogs):
            self.__y += 35
            self.button.append(
                Button(
                        image = self.button_image[i],
                        borderwidth=0,
                        highlightthickness=0,
                        command=lambda c=catalog: self.switch_catalog(c),
                        relief="flat"
                    )
            )
            self.button[i].place(x=0, y= self.__y, width=self.__width,height= self.__height)

        # Create the cart and payment buttons

        # build_button = tk.Button(self.__master, text="show Build", command=self.show_build)
        # build_button.pack(side="right")
        button_image_1 = PhotoImage(file=relative_to_assets("button_12.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_checkout,
            relief="flat"
        )
        self.button_1.place(x=1101.0, y=552.0, width=117.0, height=29.25)
        
        
        # button_image_2 = PhotoImage(file=relative_to_assets("button_11.png"))
        # self.button_2 = Button(
        #     image=button_image_2,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_2 clicked"),
        #     relief="flat"
        # )
        # self.button_2.place(x=23.0, y=531.0, width=130.0, height=36.0)
        
        self.__frame = tk.Frame(self.__master)
        self.__frame.pack(padx=350, pady=0, anchor="w")

        self.__status_label = tk.Label(self.__master, text='')
        self.__status_label.pack()
        # Create the frame for the products
        self.__master.resizable(False, False)
        self.__master.mainloop()
        
    def open_checkout(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = ProductcheckoutGUI(checkout_window)
        checkout_window.mainloop()

        # Display the initial catalog
        self.switch_catalog(self.__catalogs[0])

    # Function to add a product to the cart
    def add_to_build(self, catalog, product):
        url = f"http://localhost:8000/build/add/{catalog}"
        prod = {'id': product['id']}
        response = requests.post(url, json=prod)
        if response.status_code == 200:
            data = response.json()
            messagebox.showinfo('status : ', 'Successfully added product')
            # self.__status_label.config(text=f"{data}")
        else:
             messagebox.showinfo({'status', 'Failed to added product'})

    def open_checkout(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        catalog_ui = ProductcheckoutGUI(checkout_window)
        checkout_window.mainloop()
    
    # Function to switch catalogs
    def switch_catalog(self, catalog):
        # Clear the frame
        for widget in self.__frame.winfo_children():
            widget.destroy()

        self.__status_label.config(text="")
        # Get the products from the API
        url = f"http://localhost:8000/products/{catalog}"
        response = requests.get(url)
        products = json.loads(response.text)

        # Display the products in the catalog
        for product in products:
            img = Image.open(product['thumbnail_url'])
            img = img.resize((70, 70), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.__frame, image=photo)
            label.image = photo  # to prevent image garbage collection
            label.pack()

            button = tk.Button(self.__frame, text=product["full_name"], command= lambda c=catalog, p=product: self.add_to_build(c, p),)
            button.pack(anchor="w", pady=10)
    

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
            command=lambda: self.open_back_catalog(),
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
            command=lambda: self.open_waytopay(),
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
    ASSETS_PATH = OUTPUT_PATH / Path(r"./build_checkout/assets/frame0")

    def relative_to_assets1(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def relative_to_assets(self, path: str) -> Path:
        return Path(path)
    
    def open_back_catalog(self):
        self.master.destroy()
        checkout_window = tk.Tk()
        login_gui = ProductCatalogGUI(checkout_window)
        checkout_window.mainloop()
        
    def open_waytopay(self):
        self.master.destroy()
        checkout_window = tk.Tk()
        login_gui = Way_to_pay(checkout_window)
        checkout_window.mainloop()

        # Display the initial catalog
        # self.switch_catalog(self.__catalogs[0])
# class ProductcheckoutGUI:
#     def __init__(self, master):
#         self.__master = master
#         self.__master.title("Product Checkout")
#         screen_width = self.__master.winfo_screenwidth()
#         screen_height = self.__master.winfo_screenheight()
#         window_width = screen_width
#         window_height = screen_height
#         self.__master.geometry(f"{window_width}x{window_height}")

#         payment_button = tk.Button(self.__master, text="payment",bg="green",command = self.open_waytopay)
#         payment_button.pack(side="right",anchor="se")

#         back_button = tk.Button(self.__master, text="back",bg="#FFA500",command=self.open_back_catalog)
#         back_button.pack(side="left",anchor="sw", padx=1.5)

#         # Display Builds
#         self.show_checkout()
        
#     # Function to display the cart
#     def show_checkout(self):
#         url = "http://localhost:8000/build"
#         response = requests.get(url)
#         build = json.loads(response.text)
#         if len(build) == 0:
#             tk.Label(self.__master, text="Build: Your build is empty.").pack()
#         else:
#             for product in build:
#                 img = Image.open(product['thumbnail_url'])
#                 img = img.resize((60, 60), Image.ANTIALIAS)
#                 photo = ImageTk.PhotoImage(img)
#                 label = tk.Label(self.__master, image=photo)
#                 label.image = photo  # to prevent image garbage collection
#                 label.pack()

#                 button = tk.Label(self.__master, text=product["full_name"])
#                 button.pack(anchor="w", pady=1)
#             url = "http://localhost:8000/build/price"
#             response = requests.get(url)
#             price = json.loads(response.text)
#             t = tk.Label(self.__master, text=str(price['price']) + ' baht')
#             t.pack(anchor="ne", pady=1)



    
class Way_to_pay:
    def __init__(self, master):
        self.__master = master
        self.__master.title("OOP Spec")
        self.__master.geometry("1240x600")
        self.__master.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.__master,
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
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./build_waytopay/assets/frame0")
        
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
            command=lambda: self.open_checkout(),
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
            command=lambda: self.open_paybycard(),
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
            command=lambda: self.open_paybytransfer(),
            relief="flat"
        )
        self.button_3.place(
            x=405.0,
            y=300.0,
            width=448.0,
            height=75.0
        )
        
        self.__master.resizable(False, False)
    def open_checkout(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = ProductcheckoutGUI(checkout_window)
        checkout_window.mainloop()
        
    def open_paybycard(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = Paybycard(checkout_window)
        checkout_window.mainloop()
        
    def open_paybytransfer(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = Paybyqr(checkout_window)
        checkout_window.mainloop()
        
class Paybyqr:
    
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
            command=lambda: self.open_final(),
            relief="flat"
        )
        self.button_1.place(
            x=1061.0,
            y=511.0,
            width=148.0,
            height=64.0
        )
        
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

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            808.0,
            314.0,
            image=self.image_image_2
        )
        
        self.__master.resizable(False, False)
    def open_waytopay(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = Way_to_pay(checkout_window)
        checkout_window.mainloop()
        
    def open_final(self):
        self.__master.destroy()
        final_window = tk.Tk()
        final_gui = FinalPage(final_window)
        final_window.mainloop()
        


class Paybycard:
    def __init__(self, master):
        self.__master = master

        self.__master.geometry("1240x600")
        self.__master.configure(bg="#FFFFFF")

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./build_credit/assets/frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        self.canvas = Canvas(
            self.__master,
            bg="#FFFFFF",
            height=600,
            width=1240,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_final(),
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

        self.__master.resizable(False, False)
    def open_waytopay(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = Way_to_pay(checkout_window)
        
    def open_final(self):
        self.__master.destroy()
        final_window = tk.Tk()
        final_gui = FinalPage(final_window)

class FinalPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Payment Successful")
        self.master.geometry("1240x600")
        self.master.configure(bg="#3653E9")
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./build_final/assets/frame0")

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
            command=lambda: self.open_login(),
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
    def open_login(self):
        self.master.destroy()
        openlogin_window = tk.Tk()
        login_gui = LoginGUI(openlogin_window)
        openlogin_window.mainloop()
root = tk.Tk()
login_gui = LoginGUI(root)
root.mainloop()