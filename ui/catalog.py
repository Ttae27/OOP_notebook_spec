class Catalog():
    def __init__(self, product_class) -> None:
        self.__product_class = product_class

    def list_product(self, cat: str, filter: dict) -> list:
        products = self.__product_class.get_product(cat, filter)
        product_list = []
        for product in products:
            product_list.append({key.replace(f"_{type(product).__name__}__", ""): value for key, value in vars(product).items()})
        return product_list

    def search(self, cat: str, full_name: str) -> list:
        products = self.__product_class.get_product(cat, {"full_name": full_name})
        product_list = []
        for product in products:
            product_list.append({key.replace(f"_{type(product).__name__}__", ""): value for key, value in vars(product).items()})
        return product_list

    def get_item(self, cat: str, product_id: int) -> list:
        products = self.__product_class.get_product(cat, {'id': [product_id]})
        product_list = []
        for product in products:
            product_list.append({key.replace(f"_{type(product).__name__}__", ""): value for key, value in vars(product).items()})
        return product_list
    
