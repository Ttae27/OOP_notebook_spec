from ui.Product import Product

class GPU(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

    # def __str__(self):
    #     return f"{self.model}"