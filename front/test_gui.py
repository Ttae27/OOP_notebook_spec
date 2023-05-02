# #Import the required libraries
# from tkinter import *

# #Create an instance of tkinter frame
# win= Tk()

# #Set the geometry of frame
# win.geometry("650x250")

# #Define a function to clear the Entry Widget Content
# def clear_text():
#    text.delete(0, END)

# #Create a entry widget
# text= Entry(win, width=40)
# text.pack()

# #Create a button to clear the Entry Widget
# Button(win,text="Clear", command=clear_text, font=('Helvetica bold',10)).pack(pady=5)

# win.mainloop()

import tkinter as tk

class ProductGrid(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.catalogs = {
            'Catalog 1': [
                {'name': 'Product 1', 'price': '$10'},
                {'name': 'Product 2', 'price': '$20'},
                {'name': 'Product 3', 'price': '$30'},
                {'name': 'Product 4', 'price': '$40'},
                {'name': 'Product 5', 'price': '$50'},
                {'name': 'Product 6', 'price': '$60'}
            ],
            'Catalog 2': [
                {'name': 'Product A', 'price': '$15'},
                {'name': 'Product B', 'price': '$25'},
                {'name': 'Product C', 'price': '$35'},
                {'name': 'Product D', 'price': '$45'}
            ]
        }
        self.current_catalog = None
        self.grid_rowconfigure(3, weight=1)  # Set the 4th row to expand vertically
        self.create_widgets()
        self.show_catalog('Catalog 1')  # Show initial catalog

    def create_widgets(self):
        self.catalog_select = tk.StringVar()
        self.catalog_select.set('Catalog 1')
        self.catalog_menu = tk.OptionMenu(self, self.catalog_select, *self.catalogs.keys(), command=self.on_catalog_select)
        self.catalog_menu.grid(row=0, column=0, columnspan=3, pady=10)

        self.product_frames = []

    def on_catalog_select(self, catalog):
        self.clear_product_frames()
        self.show_catalog(catalog)

    def clear_product_frames(self):
        for frame in self.product_frames:
            frame.destroy()
        self.product_frames = []

    def show_catalog(self, catalog):
        self.current_catalog = catalog
        products = self.catalogs[catalog]
        row = 1
        col = 0
        for product in products:
            product_frame = tk.Frame(self)
            product_frame.grid(row=row, column=col, padx=10, pady=10)

            # Add product information to the frame
            label_name = tk.Label(product_frame, text=product['name'])
            label_name.pack()

            label_price = tk.Label(product_frame, text=product['price'])
            label_price.pack()

            self.product_frames.append(product_frame)

            col += 1
            if col > 2:
                col = 0
                row += 1

root = tk.Tk()
product_grid = ProductGrid(root)
product_grid.pack()

root.mainloop()


# import requests
# from PIL import Image
# from io import BytesIO
# import tkinter

# # Set the image URL
# url = 'https://notebookspec.com/storage/pc-cpu/491-1.png'

# # Make a request to the URL
# response = requests.get(url)

# # Convert the content of the response to an image
# img = Image.open(BytesIO(response.content))

# # Display the image
# img.show()

