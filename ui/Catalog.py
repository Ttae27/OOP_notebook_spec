from ui.Product import Product as product

class Catalog():

    def list(cat :str, filter :dict, sort :int):
        products = product.get(type, filter)
        #*sort products
        return products

    def get_item(cat, name):
        return product.get(cat, "full_name", name)

    def search(cat, filter_type, filter):
        pass


