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
        self.__master = master
        self.__master.title("Product Checkout")
        screen_width = self.__master.winfo_screenwidth()
        screen_height = self.__master.winfo_screenheight()
        window_width = screen_width
        window_height = screen_height
        self.__master.geometry(f"{window_width}x{window_height}")

        payment_button = tk.Button(self.__master, text="payment",bg="green")
        payment_button.pack(side="right",anchor="se")

        back_button = tk.Button(self.__master, text="back",bg="#FFA500",command=self.open_back_catalog)
        back_button.pack(side="left",anchor="sw", padx=1.5)

        # Display Builds
        self.show_checkout()
        
    # Function to display the cart
    def show_checkout(self):
        url = "http://localhost:8000/build"
        response = requests.get(url)
        build = json.loads(response.text)
        if len(build) == 0:
            tk.Label(self.__master, text="Build: Your build is empty.").pack()
        else:
            for product in build:
                img = Image.open(product['thumbnail_url'])
                img = img.resize((60, 60), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                label = tk.Label(self.__master, image=photo)
                label.image = photo  # to prevent image garbage collection
                label.pack()

                button = tk.Label(self.__master, text=product["full_name"])
                button.pack(anchor="w", pady=1)
            url = "http://localhost:8000/build/price"
            response = requests.get(url)
            price = json.loads(response.text)
            t = tk.Label(self.__master, text=str(price['price']) + ' baht')
            t.pack(anchor="ne", pady=1)


    def open_back_catalog(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = ProductCatalogGUI(checkout_window)
        checkout_window.mainloop()


root = tk.Tk()
login_gui = LoginGUI(root)
root.mainloop()