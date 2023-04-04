class Product():
    def __init__(self, model, specification, warranty, price):
        self.model =  model
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
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class Cooling(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class CPU(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class GPU(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model
    
class Monitor(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class Motherboard(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class PSU(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class RAM(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class Storage(Product):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class HDD(Storage):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class SSD(Storage):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

class M_dot_2(SSD):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model

class SATA(SSD):
    def __init__(self, model, specification, warranty, price):
        super().__init__(model, specification, warranty, price)
        self.type = __class__.__name__

    def __str__(self):
        return self.model