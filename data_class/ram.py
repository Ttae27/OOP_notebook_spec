class RAM:
    def __init__(self,
                id :int,
                series :str,
                model :str,
                type :str,
                capa :str,
                bus :int,
                latency :str,
                vol :float,
                color :int,
                warranty :str,
                ram_unit :int,
                brand_name :str,
                full_name :str,
                price :int,
                thumbnail_url :str
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
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price