class RAM:
    def __init__(self,
                id: int,
                series: str,
                model: str,
                type: str,
                capa: str,
                bus: int,
                latency: str,
                vol: float,
                color: int,
                warranty: str,
                ram_unit: int,
                brand_name: str,
                full_name: str,
                price: int,
                thumbnail_url: str
                ):

        self.__id = id
        self.__series = series
        self.__model = model
        self.__type = type
        self.__capa = capa
        self.__bus = bus
        self.__latency = latency
        self.__vol = vol
        self.__color = color
        self.__warranty = warranty
        self.__ram_unit = ram_unit
        self.__brand_name = brand_name
        self.__full_name = full_name
        self.__price = price
        self.__thumbnail_url = thumbnail_url

    @property
    def id(self):
        return self.__id

    @property
    def series(self):
        return self.__series

    @property
    def model(self):
        return self.__model

    @property
    def type(self):
        return self.__type

    @property
    def capa(self):
        return self.__capa

    @property
    def bus(self):
        return self.__bus

    @property
    def latency(self):
        return self.__latency

    @property
    def vol(self):
        return self.__vol

    @property
    def color(self):
        return self.__color

    @property
    def warranty(self):
        return self.__warranty

    @property
    def ram_unit(self):
        return self.__ram_unit

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