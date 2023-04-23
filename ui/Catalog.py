from ui.Product import Product as product

class Catalog():
    def __init__(self, product_class) -> None:
        self.__product_class = product_class

    def list(self, cat :str, filter :dict):
        products = self.__product_class.get_product(cat, filter)
        lst = []
        for product in products:
            lst.append(vars(product))
        return lst

    def get_item(self, cat :str, product_id :str):
        return self.__product_class.get_product(cat, {'id': [product_id]})

    def search(self, cat, full_name):
        products = self.__product_class.get_product(cat, {'full_name': full_name})
        return products
