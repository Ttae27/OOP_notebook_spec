from ui.Product import Product

class Case(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)