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
            'monitor': False,
            'pc_case': False,
            'psu': False,
            'ram': False,
            'ssd': False
        }
    #return product instance base on id
    def get_product_from_id(self, cat: str, product_id: int) -> object:
        product_instance = self.__product_class.get_product(cat, {'id':[product_id]})
        return product_instance

    def add_to_build(self, cat: str, product_id: int) -> list:
        product = self.get_product_from_id(cat, product_id)
        #if there is already a product in that category, it'll be removed.
        if self.__build_status[cat]:
            self.remove_from_build(cat)
        #add new product to build.
        self.__build.extend(product)
        #after add the product, set the status that the product of that category is now exist.
        self.__build_status[cat] = True
        return self.__build

    def remove_from_build(self, id: int) -> list:
        for product in self.__build:
            if product.__getattribute__('id') == id:
                existing_product = product
        self.__build.remove(existing_product)
        return self.__build
    
    def cal_price(self,cart):
        self.__cart = cart
        for product in range(len(self.__cart)):
            self.__totalprice = self.__totalprice + cart[product].price
        return self.__totalprice
        
    @property
    #get total price from build
    def totalprice(self):
        return self.__totalprice
    
    @property
    #todo add function to convert list of object to dict
    def build(self):
        return self.__build

