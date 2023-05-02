class Build:
    def __init__(self, product_class: object) -> None:
        self.__build = []
        self.__totalprice = 0
        self.__product_class = product_class
        self.__build_status = {
            'cooling': False,
            'cpu': False,
            'gpu': False,
            'hdd': False,
            'motherboard': False,
            'monitor': False,
            'pc_case': False,
            'psu': False,
            'ram': False,
            'ssd': False
        }

    def add_to_build(self, cat: str, product_id: int) -> list:
        product = self.__product_class.get_product(cat, {'id':[product_id]})
        if self.__build_status[cat]:
            id_to_rm = self.__build_status[cat][0].id
            self.remove_from_build(id_to_rm)
        #add new product to build.
        self.__build.extend(product)
        #after add the product, also add to dict
        self.__build_status[cat] = product
        return {'Status': 'Successfully added to build'}

    def remove_from_build(self, id: int) -> list:
        for product in self.__build:
            if product.__getattribute__('id') == id:
                existing_product = product
        self.__build.remove(existing_product)
        return self.__build
    
    def cal_price(self):
        totalprice = 0
        for product in self.__build:
            totalprice = totalprice + product.price
        self.__totalprice = totalprice
        return self.__totalprice
        
    def show_build(self):
        product_in_build = []
        if len(self.__build) != 0:
            for product in self.__build:
                product_in_build.append({key.replace(f"_{type(product).__name__}__", ""): value for key, value in vars(product).items()})
        return product_in_build
    
    @property
    def totalprice(self):
        return self.__totalprice
    
    @property
    def build(self):
        return self.__build

