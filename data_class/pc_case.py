class PC_Case:
    def __init__(self,
                id: int,
                model: str,
                mat: str,
                color: str,
                weight: str,
                dimension: str,
                io: str,
                warranty: int,
                active: int,
                brand_name: str,
                full_name: str,
                price: int,
                thumbnail_url: str):

        self.__id = id
        self.__model = model
        self.__mat = mat
        self.__color = color
        self.__weight = weight
        self.__dimension = dimension
        self.__io = io
        self.__warranty = warranty
        self.__active = active
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
    def mat(self):
        return self.__mat

    @property
    def color(self):
        return self.__color

    @property
    def weight(self):
        return self.__weight

    @property
    def dimension(self):
        return self.__dimension

    @property
    def io(self):
        return self.__io

    @property
    def warranty(self):
        return self.__warranty

    @property
    def active(self):
        return self.__active

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
            print("Please enter valid price") #! need to change this