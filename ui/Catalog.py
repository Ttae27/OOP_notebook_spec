from ui.Product import Product as product
from urllib.parse import unquote
import json
class Catalog():
    def __init__(self) -> None:
        pass

    def list(self, cat :str, filter :dict, sort :int):
        products = product.get(cat, filter)
        #*sort products
        return products

    def get_item(self, cat, name):
        return product.get(cat, "full_name", name)

    def search(self, cat, filter_type, filter):
        pass

