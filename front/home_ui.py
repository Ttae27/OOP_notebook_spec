import tkinter as tk
from tkinter import ttk
import requests
import json
import tkinter as tk
from urllib.parse import unquote
from PIL import Image, ImageTk
from tkinter import messagebox

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
        screen_width = self.__master.winfo_screenwidth()
        screen_height = self.__master.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        self.__master.geometry(f"{window_width}x{window_height}")
        self.login_status_button = ""
        master.title("Login")

        # Create username label and entry
        self.__username_label = tk.Label(master, text="Username:")
        self.__username_label.pack()
        self.__username_entry = tk.Entry(master)
        self.__username_entry.pack()

        # Create password label and entry
        self.__password_label = tk.Label(master, text="Password:")
        self.__password_label.pack()
        self.__password_entry = tk.Entry(master, show="*")
        self.__password_entry.pack()

        # Create login button and switch to catalog page
        self.__login_button = tk.Button(master, text="Login",bg="#FFA500", command=self.open_catalog)
        self.__login_button.pack()

        self.__status_label = tk.Label(master, text='')
        self.__status_label.pack()
        

    def login(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()

        credential = {'username': username, 'password': password}
        response = requests.post('http://localhost:8000/signin', json=credential)
        data = response.json()
        self.__status_label.config(text=f"{data}")
        return data

    def open_catalog(self):
        # print(self.login_status_button)
        data = self.login()
        if data == {"Status": "log in successfully"}:
            self.__master.destroy()
            catalog_window = tk.Tk()
            login_gui = ProductCatalogGUI(catalog_window)
            catalog_window.mainloop()

class SignupGUI:
    def __init__(self, master):
        self.__master = master
        screen_width = self.__master.winfo_screenwidth()
        screen_height = self.__master.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        self.__master.geometry(f"{window_width}x{window_height}")
        master.title("Sign Up")

        # Create username label and entry
        self.__username_label = tk.Label(master, text="Username:")
        self.__username_label.pack()
        self.__username_entry = tk.Entry(master)
        self.__username_entry.pack()

        # Create password label and entry
        self.__password_label = tk.Label(master, text="Password:")
        self.__password_label.pack()
        self.__password_entry = tk.Entry(master, show="*")
        self.__password_entry.pack()

        # Create address label and entry
        self.__address_label = tk.Label(master, text="Address:")
        self.__address_label.pack()
        self.__address_entry = tk.Entry(master)
        self.__address_entry.pack()

        # Create phone label and entry
        self.__phone_label = tk.Label(master, text="Phone:")
        self.__phone_label.pack()
        self.__phone_entry = tk.Entry(master)
        self.__phone_entry.pack()

        # Create sign up button
        self.__signup_button = tk.Button(master, text="Sign Up",bg="#FFA500", command=self.signup)
        self.__signup_button.pack()
        

        self.__home_button = tk.Button(master, text="Home", command=self.open_home)
        self.__home_button.pack()

        self.__status_label = tk.Label(master, text='')
        self.__status_label.pack()
        
    def open_home(self):
        self.__master.destroy()
        catalog_window = tk.Tk()
        login_gui = HomePageGUI(catalog_window)
        catalog_window.mainloop()

    def signup(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()
        address = self.__address_entry.get()
        phone = self.__phone_entry.get()

        user_data = {'username': username, 'password': password, 'delivery_address': address, 'phone': phone}
        response = requests.post('http://localhost:8000/signup', json=user_data)
        data = response.json()
        self.__status_label.config(text=f"{data}")
        
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
        screen_width = self.__master.winfo_screenwidth()
        screen_height = self.__master.winfo_screenheight()
        window_width = screen_width 
        window_height = screen_height 
        self.__master.geometry(f"{window_width}x{window_height}")
        self.__master.title("Product Catalog")

        # Create the catalog buttons
        self.__catalog_buttons = []
        self.__catalogs = ["cpu", "gpu", "cooling", "hdd", "monitor", "motherboard", "pc_case", "psu", "ram", "ssd"]
        for catalog in self.__catalogs:
            button = tk.Button(self.__master, text=catalog, command=lambda c=catalog: self.switch_catalog(c))
            button.pack(side="left", padx=1.5)
            self.__catalog_buttons.append(button)

        # Create the cart and payment buttons

        # build_button = tk.Button(self.__master, text="show Build", command=self.show_build)
        # build_button.pack(side="right")
        self.__checkout_button = tk.Button(self.__master, text="Checkout",bg="green", command=self.open_checkout)
        self.__checkout_button.pack(side="right")

        # Create the frame for the products
        self.__frame = tk.Frame(self.__master)
        self.__frame.pack(padx=10, pady=10, anchor="w")

        self.__status_label = tk.Label(master, text='')
        self.__status_label.pack()
        
    def open_checkout(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = ProductcheckoutGUI(checkout_window)
        checkout_window.mainloop()

        # Display the initial catalog
        self.switch_catalog(self.__catalogs[0])

    # Function to add a product to the cart
    def add_to_build(self, catalog, product):
        url = f"http://localhost:8000/products/{catalog}"
        prod = {'id': product['id']}
        response = requests.post(url, json=prod)
        if response.status_code == 200:
            data = response.json()
            self.__status_label.config(text=f"{data}")
        # self.switch_catalog(catalog)

    # Function to display the cart
    def show_build(self):
        url = "http://localhost:8000/build"
        response = requests.get(url)
        build = json.loads(response.text)
        if len(build) == 0:
            messagebox.showinfo("show build","Build: Your build is empty.")
        else:
            for product in build:
                messagebox.showinfo("show build","Build: there are somethings in your Build.")

                img = Image.open(product['thumbnail_url'])
                img = img.resize((100, 100), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                label = tk.Label(self.__master, image=photo)
                label.image = photo  # to prevent image garbage collection
                label.pack()

                button = tk.Label(self.__master, text=product["full_name"])
                button.pack(anchor="w", pady=1)

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
            img = img.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.__frame, image=photo)
            label.image = photo  # to prevent image garbage collection
            label.pack()

            button = tk.Button(self.__frame, text=product["full_name"], command=lambda c=catalog, p=product: self.add_to_build(c, p))
            button.pack(anchor="w", pady=1)
    
    

class ProductcheckoutGUI:
    def __init__(self, master):
        self.__master = master
        self.__master.title("Product Checkout")
        screen_width = self.__master.winfo_screenwidth()
        screen_height = self.__master.winfo_screenheight()
        window_width = screen_width
        window_height = screen_height
        self.__master.geometry(f"{window_width}x{window_height}")

        # # Create the catalog buttons
        # self.__catalog_buttons = []
        # self.__catalogs = ["cpu", "gpu", "cooling", "hdd", "monitor", "motherboard", "pc_case", "psu", "ram", "ssd"]
        # for catalog in self.__catalogs:
        #     button = tk.Button(self.__master, text=catalog, command=lambda c=catalog: self.switch_catalog(c))
        #     button.pack(side="left", padx=1.5)
        #     self.__catalog_buttons.append(button)

        # Create the cart and payment buttons
        payment_button = tk.Button(self.__master, text="payment",bg="green")
        payment_button.pack(side="right",anchor="se")

        back_button = tk.Button(self.__master, text="back",bg="#FFA500",command=self.open_back_catalog)
        back_button.pack(side="left",anchor="sw", padx=1.5)
        # # Create the frame for the products
        # self.__frame = tk.Frame(self.__master)
        # self.__frame.pack(padx=10, pady=10, anchor="w")

        # self.__status_label = tk.Label(master, text='')
        # self.__status_label.pack()

        # Display Builds
        self.show_checkout()

    # Function to display the cart
    def show_checkout(self):
        url = "http://localhost:8000/build"
        response = requests.get(url)
        build = json.loads(response.text)
        if len(build) == 0:
            # messagebox.showinfo("show build","Build: Your build is empty.")
            tk.Label(self.__master, text="Build: Your build is empty.").pack()
        else:
            for product in build:
                # messagebox.showinfo("show build","Build: there are somethings in your Build.")

                img = Image.open(product['thumbnail_url'])
                img = img.resize((100, 100), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                label = tk.Label(self.__master, image=photo)
                label.image = photo  # to prevent image garbage collection
                label.pack()

                button = tk.Label(self.__master, text=product["full_name"])
                button.pack(anchor="w", pady=1)


    def open_back_catalog(self):
        self.__master.destroy()
        checkout_window = tk.Tk()
        login_gui = ProductCatalogGUI(checkout_window)
        checkout_window.mainloop()


root = tk.Tk()
login_gui = HomePageGUI(root)
root.mainloop()