import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Product Catalog")

# Define the catalog buttons and their respective catalogs
catalogs = {
    "CPU": ["Intel Core i7", "AMD Ryzen 5", "Intel Xeon"],
    "Motherboard": ["ASUS ROG Maximus XII", "Gigabyte Aorus Elite", "MSI MPG Z490"],
    "GPU": ["NVIDIA GeForce RTX 3080", "AMD Radeon RX 6800 XT", "NVIDIA Quadro RTX 5000"],
    "Memory": ["Corsair Vengeance RGB Pro 32GB", "G.Skill Trident Z RGB 16GB", "Kingston HyperX Fury 8GB"],
    "SSD": ["Samsung 970 EVO Plus 1TB", "Crucial MX500 500GB", "Western Digital Black SN850 2TB"],
    "HHD": ["Seagate Barracuda 4TB", "Western Digital Red 8TB", "Toshiba N300 12TB"],
    "PSU": ["EVGA SuperNOVA 850W", "Corsair RM750x", "Seasonic Focus GX-750"],
    "CPU Cooler": ["Noctua NH-D15", "Cooler Master Hyper 212", "be quiet! Dark Rock Pro 4"],
    "Monitor": ["LG 27GL850-B 27 inch", "ASUS TUF Gaming VG27AQ 27 inch", "Dell UltraSharp U2719D 27 inch"]
}

# Define the cart
cart = []

# Function to add a product to the cart
def add_to_cart(product):
    cart.append(product)

# Function to display the cart
def show_cart():
    if len(cart) == 0:
        tk.messagebox.showinfo("Cart", "Your cart is empty.")
    else:
        cart_text = "\n".join(cart)
        tk.messagebox.showinfo("Cart", cart_text)

# Function to switch catalogs
def switch_catalog(catalog):
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Display the products in the selected catalog
    for product in catalogs[catalog]:
        button = tk.Button(frame, text=product, command=lambda p=product: add_to_cart(p))
        button.pack()

# Create the catalog buttons
for catalog in catalogs:
    button = tk.Button(root, text=catalog, command=lambda c=catalog: switch_catalog(c))
    button.pack(side="left")

# Create the cart and payment buttons
cart_button = tk.Button(root, text="Cart", command=show_cart)
cart_button.pack(side="right")
payment_button = tk.Button(root, text="Payment")
payment_button.pack(side="right")

# Create the frame for the products
frame = tk.Frame(root)
frame.pack()

# Display the initial catalog (CPU)
switch_catalog("CPU")

# Start the main event loop
root.mainloop()
