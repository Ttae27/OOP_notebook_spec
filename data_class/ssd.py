class SSD:
    def __init__(self,
                id :int,
                model :str,
                form_factor :str,
                capacity :str,
                interface :str,
                protocal :str,
                read :int,
                write :int,
                max_4k_random :str,
                modules :str,
                endurance :str,
                technology :str,
                warranty :int,
                brand_name :str,
                full_name :str,
                permalink :str,
                price :int,
                thumbnail_url :str
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
    def price(self):
        return self.__price