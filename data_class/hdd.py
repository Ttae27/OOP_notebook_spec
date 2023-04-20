class HDD:
    def __init__(self,
                id: int,
                model: str,
                form_factor: float,
                capacity: str,
                interface: str,
                rpm: int,
                buffer: str,
                warranty: int,
                brand_name: str,
                full_name: str,
                price: int,
                thumbnail_url: str
                ):

        self.__id = id
        self.__model = model
        self.__form_factor = form_factor
        self.__capacity = capacity
        self.__interface = interface
        self.__rpm = rpm
        self.__buffer = buffer
        self.__warranty = warranty
        self.__brand_name = brand_name
        self.__full_name = full_name
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
    def rpm(self):
        return self.__rpm
    
    @property
    def buffer(self):
        return self.__buffer
    
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