import requests
import json
import tkinter as tk
from urllib.parse import unquote
from PIL import Image, ImageTk

class ProductCatalogGUI:
    def __init__(self, master):
        self.__master = master
        self.__master.title("Product Catalog")

        # Define the cart
        self.__cart = []

        # Create the catalog buttons
        self.__catalog_buttons = []
        self.__catalogs = ["cpu", "gpu", "cooling", "hdd", "monitor", "motherboard", "pc_case", "psu", "ram", "ssd"]
        for catalog in self.__catalogs:
            button = tk.Button(self.__master, text=catalog, command=lambda c=catalog: self.switch_catalog(c))
            button.pack(side="left", padx=1.5)
            self.__catalog_buttons.append(button)

        

        # Create the cart and payment buttons
        cart_button = tk.Button(self.__master, text="Cart", command=self.show_cart)
        cart_button.pack(side="right")
        payment_button = tk.Button(self.__master, text="Payment")
        payment_button.pack(side="right")

        # Create the frame for the products
        self.__frame = tk.Frame(self.__master)
        self.__frame.pack(padx=10, pady=10, anchor="w")

        # Display the initial catalog
        self.switch_catalog(self.__catalogs[0])

    # Function to add a product to the cart
    def add_to_cart(self, product):
        self.__cart.append(product)

    # Function to display the cart
    def show_cart(self):
        if len(self.__cart) == 0:
            tk.Label(self.__master, text="Cart: Your cart is empty.")
        else:
            cart_text = "\n".join(self.__cart)
            tk.Label(self.__master, text=f"Cart: {cart_text}")

    # Function to switch catalogs
    def switch_catalog(self, catalog):
        # Clear the frame
        for widget in self.__frame.winfo_children():
            widget.destroy()

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

            button = tk.Button(self.__frame, text=product["full_name"], command=lambda p=product["full_name"]: self.add_to_cart(p))
            button.pack(anchor="w", pady=1)


# Create GUI window
root = tk.Tk()
product_catalog_gui = ProductCatalogGUI(root)
root.mainloop()
