import requests
import json
import tkinter as tk
from urllib.parse import unquote
from PIL import Image, ImageTk
from tkinter import messagebox
class ProductCatalogGUI:
    def __init__(self, master):
        self.__master = master
        self.__master.title("Product Catalog")

        # Create the catalog buttons
        self.__catalog_buttons = []
        self.__catalogs = ["cpu", "gpu", "cooling", "hdd", "monitor", "motherboard", "pc_case", "psu", "ram", "ssd"]
        self.__frame1 = tk.Frame(self.__master)
        self.__frame1.pack(side= 'left', padx=100, pady=0)
        for catalog in self.__catalogs:
            button = tk.Button(self.__frame1, text=catalog, command=lambda c=catalog: self.switch_catalog(c))
            button.pack(anchor = 'w', padx = 10, pady=1.5)
            self.__catalog_buttons.append(button)

        # Create the cart and payment buttons
        # payment_button = tk.Button(self.__master, text="checkout")
        # payment_button.pack(side="right")
        # build_button = tk.Button(self.__master, text="show Build", command=self.show_build)
        # build_button.pack(side="right")

        # Create the frame for the products
        self.__frame2 = tk.Frame(self.__master)
        self.__frame2.pack(side = 'left', padx=100, pady=0)

        self.__status_label = tk.Label(master, text='')
        self.__status_label.pack()

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
        self.switch_catalog(catalog)

    # Function to display the cart
    def show_build(self):
        url = "http://localhost:8000/build"
        response = requests.get(url)
        build = json.loads(response.text)
        if len(build) == 0:
            messagebox.showinfo("show build","Build: Your build is empty.")
            # tk.Label(self.__master, text="Build: Your build is empty.")
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
        for widget in self.__frame2.winfo_children():
            widget.destroy()

        # self.__status_label.config(text="")
        # Get the products from the API
        url = f"http://localhost:8000/products/{catalog}"
        response = requests.get(url)
        products = json.loads(response.text)

        # Display the products in the catalog
        for product in products:
            img = Image.open(product['thumbnail_url'])
            img = img.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.__frame2, image=photo)
            label.image = photo  # to prevent image garbage collection
            label.pack()

            button = tk.Button(self.__frame2, text=product["full_name"], command=lambda c=catalog, p=product: self.add_to_build(c, p))
            button.pack(anchor="w", pady=1)

class ProductcheckoutGUI:
    def __init__(self, master):
        self.__master = master
        self.__master.title("Product Checkout")
        master.minsize(width = 400, height= 400)

        # # Create the catalog buttons
        # self.__catalog_buttons = []
        # self.__catalogs = ["cpu", "gpu", "cooling", "hdd", "monitor", "motherboard", "pc_case", "psu", "ram", "ssd"]
        # for catalog in self.__catalogs:
        #     button = tk.Button(self.__master, text=catalog, command=lambda c=catalog: self.switch_catalog(c))
        #     button.pack(side="left", padx=1.5)
        #     self.__catalog_buttons.append(button)

        # Create the cart and payment buttons
        payment_button = tk.Button(self.__master, text="payment")
        payment_button.pack(side="right",anchor="se")

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

# Create GUI window
root = tk.Tk()
product_catalog_gui = ProductCatalogGUI(root)
root.mainloop()
