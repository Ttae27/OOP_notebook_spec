class SSD:
    def __init__(self,
                id: int,
                model: str,
                form_factor: str,
                capacity: str,
                interface: str,
                protocal: str,
                read: int,
                write: int,
                max_4k_random: str,
                modules: str,
                endurance: str,
                technology: str,
                warranty: int,
                brand_name: str,
                full_name: str,
                permalink: str,
                price: int,
                thumbnail_url: str
                ):

        self.__id = id
        self.__model = model
        self.__form_factor = form_factor
        self.__capacity = capacity
        self.__interface = interface
        self.__protocal = protocal
        self.__read = read
        self.__write = write
        self.__max_4k_random = max_4k_random
        self.__modules = modules
        self.__endurance = endurance
        self.__technology = technology
        self.__warranty = warranty
        self.__brand_name = brand_name
        self.__full_name = full_name
        self.__permalink = permalink
        self.__price = price
        self.__thumbnail_url = thumbnail_url
    
    @property
    def id(self):
        return self.__id

    @property
    def model(self):
        return self.__model

    @property
    def form_factor(self):
        return self.__form_factor

    @property
    def capacity(self):
        return self.__capacity

    @property
    def interface(self):
        return self.__interface

    @property
    def protocal(self):
        return self.__protocal

    @property
    def read(self):
        return self.__read

    @property
    def write(self):
        return self.__write

    @property
    def max_4k_random(self):
        return self.__max_4k_random

    @property
    def modules(self):
        return self.__modules

    @property
    def endurance(self):
        return self.__endurance

    @property
    def technology(self):
        return self.__technology

    @property
    def warranty(self):
        return self.__warranty

    @property
    def brand_name(self):
        return self.__brand_name

    @property
    def full_name(self):
        return self.__full_name

    @property
    def permalink(self):
        return self.__permalink

    @property
    def price(self):
        return self.__price

    @property
    def thumbnail_url(self):
        return self.__thumbnail_url

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) and new_price > 0:
            self.__price = new_price
        else:
            print("Please enter valid price") #!need to change this