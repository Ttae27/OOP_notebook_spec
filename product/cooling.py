from ui.Product import Product

class Cooling(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)