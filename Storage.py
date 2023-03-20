import Product

class Storage(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class HDD(Storage):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class SSD(Storage):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class M_dot_2(SSD):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class SATA(SSD):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)