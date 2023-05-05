import sys

# import data.py
sys.path.append('../oop_notebook_spec')
from data import get_product, delete_data, update_price_data, add_product_data

class Product():
    def __init__(self) -> None:
        self.current_product = [] #store the current showing product
        self.current_cat = ""

    def get_product(self, cat: str, filter :dict = None) -> list:
        #only fetch from database if cat change
        if self.current_cat != cat:
            self.current_cat = cat
            self.current_product = get_product(cat)

        #activate if there is any filter
        if filter:
            filtered_list = [
                product for product in self.current_product
                if all(
                getattr(product, key) in value_list
                for key, value_list in filter.items()
                if value_list
                )
            ]
            return filtered_list
        return self.current_product

    def update_price_product(self, cat: str, product_id: int, new_price: int) -> list:
        for product in self.current_product:
            if product.id == product_id:
                self.current_product = update_price_data(cat, product_id, new_price)
                return {'status': 'Successfully update product id ' + str(product_id)}
        return {'status': 'Failed update product'}

    def delete_product(self, cat: str, product_id: int):
        for product in self.current_product:
            if product.id == product_id:
                self.current_product = delete_data(cat, product_id)
                return {'status': 'Successfully delete product ' + str(product_id)}
        return {'status': 'Failed delete product'}

    def add_product(self, cat: str, new_product: dict):
        for product in self.current_product:
            if product.id == new_product['id']:
                return {'status': 'Failed to added product'}
        new_product = tuple(new_product.values())
        self.current_product = add_product_data(cat, new_product)
        return {'status': 'Successfully added product'}