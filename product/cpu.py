from ui.Product import Product

class CPU(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
