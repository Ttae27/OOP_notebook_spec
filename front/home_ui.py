import tkinter as tk
from tkinter import ttk
import requests

class HomePageGUI:
    def __init__(self, master):
        self.__master = master
        master.title("Home Page")

        # Create sign in button
        self.__signin_button = ttk.Button(master, text="Sign In", command=self.open_login)
        self.__signin_button.pack()

        # Create sign up button
        self.__signup_button = ttk.Button(master, text="Sign Up", command=self.open_signup)
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
        self.__login_button = tk.Button(master, text="Login", command=self.open_catalog)
        self.__login_button.pack()

        self.__status_label = tk.Label(master, text='')
        self.__status_label.pack()
        
    def open_catalog(self):
        self.__master.destroy()
        catalog_window = tk.Tk()
        login_gui = ProductCatalogGUI(catalog_window)
        catalog_window.mainloop()

    def login(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()

        credential = {'username': username, 'password': password}
        response = requests.post('http://localhost:8000/signin', json=credential)
        data = response.json()
        self.__status_label.config(text=f"{data}")


class SignupGUI:
    def __init__(self, master):
        self.__master = master
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
        self.__signup_button = tk.Button(master, text="Sign Up", command=self.signup)
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
        master.title("Product Catalog")

        # Define the catalog buttons and their respective catalogs
        self.__catalogs = ["CPU", "GPU", "Cooling", "HDD", "Monitor", "Motherboard", "Case", "PSU", "RAM", "SSD"]

        # Define the cart
        self.__cart = []

        # Create the catalog buttons
        for catalog in self.__catalogs:
            button = tk.Button(master, text=catalog, command=lambda c=catalog: self.switch_catalog(c))
            button.pack(side="left")

        # Create the cart and payment buttons
        cart_button = tk.Button(master, text="Cart", command=self.show_cart)
        cart_button.pack(side="right")
        payment_button = tk.Button(master, text="Payment")
        payment_button.pack(side="right")

        # Create the frame for the products
        self.__frame = tk.Frame(master)
        self.__frame.pack()

        # Display the initial catalog (CPU)
        self.switch_catalog("CPU")

    # Function to add a product to the cart
    def add_to_cart(self, product):
        self.__cart.append(product)

    # Function to display the cart
    def show_cart(self):
        if len(self.__cart) == 0:
            tk.messagebox.showinfo("Cart", "Your cart is empty.")
        else:
            cart_text = "\n".join(self.__cart)
            tk.messagebox.showinfo("Cart", cart_text)

    # Function to switch catalogs
    def switch_catalog(self, catalog):
        # Clear the frame
        for widget in self.__frame.winfo_children():
            widget.destroy()

        # Display the products in the selected catalog
        for product in self.__catalogs[catalog]:
            button = tk.Button(self.__frame, text=product, command=lambda p=product: self.add_to_cart(p))
            button.pack()
            
root = tk.Tk()
login_gui = HomePageGUI(root)
root.mainloop()