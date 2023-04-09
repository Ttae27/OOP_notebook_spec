
class Compare():
    def __init__(self):
        self.spec_1 = {}
        self.show_spec_1 = {}
        self.spec_2 = {}
        self.show_spec_2 = {}
        
        
    def add_item(self, item, i):
        if i == "1":
            self.spec_1[type(item).__name__] = item
            self.show_spec_1[type(item).__name__] = item.model
        else:
            self.spec_2[type(item).__name__] = item
            self.show_spec_2[type(item).__name__] = item.model
        
    def remove_item(self, item, i):
        if i == "1":
            self.spec_1.pop(type(item).__name__)
            self.show_spec_1.pop(type(item).__name__)
        else:
            self.spec_2.pop(type(item).__name__)
            self.show_spec_2.pop(type(item).__name__)
        
    def compare_spec(self):
        totalPrice = 0
        for product in self.spec_1.values():
                totalPrice += int(product.price)
                self.show_spec_1["price"] = totalPrice
        totalPrice = 0
        for product in self.spec_2.values():
                totalPrice += int(product.price)
                self.show_spec_2["price"] = totalPrice
        return self.show_spec_1, self.show_spec_2
#!!there isnt compare make compare or change method name