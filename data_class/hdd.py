class HDD:
    def __init__(self, id, model, form_factor, capacity, interface, rpm, buffer, warranty, brand_name, full_name, price, thumbnail_url):
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
    def price(self):
        return self.__price