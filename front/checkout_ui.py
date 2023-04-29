import tkinter as tk

class CheckoutProductUI:
    def __init__(self, root, product):
        self.root = root
        self.product = product

        self.create_ui()

    def create_ui(self):
        # Create a frame to hold the product information
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Create a label for the product name
        name_label = tk.Label(frame, text="Product Name: ")
        name_label.pack(side=tk.LEFT)

        name_value = tk.Label(frame, text=self.product.name)
        name_value.pack(side=tk.LEFT)

        # Create a label for the product price
        price_label = tk.Label(frame, text="Price: ")
        price_label.pack(side=tk.LEFT)

        price_value = tk.Label(frame, text=self.product.price)
        price_value.pack(side=tk.LEFT)

        # Create a "Next" button
        next_button = tk.Button(self.root, text="Next", command=self.next_clicked)
        next_button.pack(pady=10)

    def next_clicked(self):
        # Handle the "Next" button click event
        # Add your logic here
        pass

root = tk.Tk()
login_gui = CheckoutProductUI(root)
root.mainloop()