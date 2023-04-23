from Product import Product #!debug only pls delete after

class Build:
    def __init__(self, product_class: object) -> None:
        self.__build = []
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

    #will return product instance giving id
    def get_product_from_id(self, cat:str, product_id: int) -> object:
        product_instance = self.__product_class.get_product(cat, {'id':[product_id]})
        return product_instance

    def add_to_build(self, cat: str, product_id: int) -> list:
        product = self.get_product_from_id(cat, product_id)
        #if there is already a product in that category, it'll be removed.
        if self.__build_status[cat]:
            self.__build.remove(self.__getattribute__(cat))
        #add new product to build.
        self.__build.extend(product)
        #after add the product, set the status that the product of that category is now exist.
        self.__build_status[cat] = True
        return self.__build

    def remove_from_build(self, cat: str, product_id: int) -> list:
        product = self.get_product_from_id(cat, {'id':[product_id]})
        #check if product exist, if not do nothing
        if self.__build_status[cat]:
            self.__build.remove(product)
        return self.__build #? should I return build here or let main.py use get method


    @property
    #todo add function to convert list of object to dict
    def build(self):
        return self.__build

#!debug only pls remove after
product = Product()
build = Build(product)

build.add_to_build('cpu', 6)
build.add_to_build('gpu', 11)

print(build.build)
print('cpu series is ' + build.build[0].series)
print('gpu series is ' + build.build[1].series)
