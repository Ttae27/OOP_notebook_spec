from Product import Product as product
class Catalog():
    def product_get(product_cat :str, filter :str, sort :str):
        current_product = product.get(product_cat, filter)
        if (sort):
            pass