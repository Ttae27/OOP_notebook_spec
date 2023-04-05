from fastapi import FastAPI
app = FastAPI()

class Compare():
    def __init__(self,build):
        self.spec_1 = {}
        self.amount_1 = 0
        self.spec_2 = {}
        self.amount_2 = 0
        
        
    def add_item(self, item, i):
        if i == 1:
            self.spec_1[type(item).__name__] = item
        else:
            self.spec_2[type(item).__name__] = item
        
    def remove_item(self, item, i):
        if i == 1:
            self.spec_1.pop(type(item).__name__)
        else:
            self.spec_2.pop(type(item).__name__)
        
    def comparespec(self):
        for product in self.spec_1.values():
                self.amount_1 += int(product.price)
                self.spec_1["price"] = self.amount_1
        for product in self.spec_2.values():
                self.amount_2 += int(product.price)
                self.spec_2["price"] = self.amount_2
        return self.spec_1, self.spec_2
        