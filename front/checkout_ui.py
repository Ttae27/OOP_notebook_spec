import requests
import json
import tkinter as tk
from urllib.parse import unquote
from PIL import Image, ImageTk
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
product_catalog_gui = ProductcheckoutGUI(root)
root.mainloop()
