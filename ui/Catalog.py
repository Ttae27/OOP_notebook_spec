from Product import Product as product

class Catalog():
    def __init__(self):
        self.catalog = {}

    def list(self, type):
        return product.get(type)

    def get_item(self, type, name):
        return product.get(type, "full_name", name)

    def search(self, type, filter_type, filter):
        

    def sort():
        pass
