class Product():
    def __init__(self, model, specification, warranty, price):
        self.model = model
        self.specification = specification
        self.warranty = warranty
        self.price = price

    def remove():
        pass

    def update():
        pass

class Case(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class Cooling(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class CPU(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class GPU(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class Monitor(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class Motherboard(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class PSU(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

class RAM(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)

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
