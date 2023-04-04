class Catalog():
    def __init__(self):
        self.catalog = {}

    def add(self, item, type):
        if type not in self.catalog:
            self.catalog[type] = []
        if item not in self.catalog[type]:
            self.catalog[type].append(item)

    def remove(self, item, type):
        if type in self.catalog and item in self.catalog[type]:
            self.catalog[type].remove(item)

    def update(self, item, new_warranty=None, new_price=None):
        for cpu in self.cpu:
            if cpu == item:
                cpu.warranty = new_warranty
                cpu.price = new_price

    def list(self, type):
        if type not in self.catalog:
            return None
        item_list = []
        for item in self.catalog[type]:
            item_list.append(item.model)
        return item_list

    def get_item(self, name):
        if name in self.catalog[name.type]:
            return name
        return None


    def display():
        pass

    def search():
        pass

    def sort():
        pass

    def filter():
        pass