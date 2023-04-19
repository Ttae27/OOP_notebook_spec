class Cooling:
    def __init__(self,
                id :int,
                series :str,
                model :str,
                type :str,
                cpu_support_intel :str,
                cpu_support_amd :str,
                dimension :str,
                material :str,
                fan_built_in :str,
                led :int,
                warranty :int,
                price :int,
                brand_name :str,
                full_name :str,
                thumbnail_url :str,
                ):

        self.__id = id
        self.__series = series
        self.__model = model
        self.__type = type
        self.__cpu_support_intel = cpu_support_intel
        self.__cpu_support_amd = cpu_support_amd
        self.__dimension = dimension
        self.__material = material
        self.__fan_built_in = fan_built_in
        self.__led = led
        self.__warranty = warranty
        self.__price = price
        self.__brand_name = brand_name
        self.__full_name = full_name
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
    def cpu_support_intel(self):
        return self.__cpu_support_intel

    @property
    def cpu_support_amd(self):
        return self.__cpu_support_amd

    @property
    def dimension(self):
        return self.__dimension

    @property
    def material(self):
        return self.__material

    @property
    def fan_built_in(self):
        return self.__fan_built_in

    @property
    def led(self):
        return self.__led

    @property
    def warranty(self):
        return self.__warranty

    @property
    def price(self):
        return self.__price

    @property
    def brand_name(self):
        return self.__brand_name

    @property
    def full_name(self):
        return self.__full_name

    @property
    def thumbnail_url(self):
        return self.__thumbnail_url

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) and new_price > 0:
            self.__price = new_price
        else:
            print("Please enter valid price")