import tkinter as tk

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

# Create GUI window
root = tk.Tk()
product_catalog_gui = ProductCatalogGUI(root)
root.mainloop()
