from ui.Product import Product as product

class Catalog():

    def list(type):
        return product.get(type)

    def get_item(type, name):
        return product.get(type, "full_name", name)

    def search(type, filter_type, filter):
        pass


