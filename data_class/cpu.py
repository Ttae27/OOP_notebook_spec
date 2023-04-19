class CPU:
    def __init__(self,
                id: int,
                series: str,
                model: str,
                socket: str,
                chipsupport: str,
                core :int,
                thread :int,
                frequency :str,
                l2 :str,
                l3 :str,
                gpu_integrated :str,
                power :str,
                warranty :int,
                active :int,
                brand_name :str, 
                full_name :str,
                price :int,
                thumbnail_url :str
                ):
        
        self.__id = id
        self.__series = series
        self.__model = model
        self.__socket = socket
        self.__chipsupport = chipsupport
        self.__core = core
        self.__thread = thread
        self.__frequency = frequency
        self.__l2 = l2
        self.__l3 = l3
        self.__gpu_integrated = gpu_integrated
        self.__power = power
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
    def series(self):
        return self.__series

    @property
    def model(self):
        return self.__model

    @property
    def socket(self):
        return self.__socket

    @property
    def chipsupport(self):
        return self.__chipsupport

    @property
    def core(self):
        return self.__core

    @property
    def thread(self):
        return self.__thread

    @property
    def frequency(self):
        return self.__frequency

    @property
    def l2(self):
        return self.__l2

    @property
    def l3(self):
        return self.__l3

    @property
    def gpu_integrated(self):
        return self.__gpu_integrated

    @property
    def power(self):
        return self.__power

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
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) and new_price > 0:
            self.__price = new_price
        else:
            print("Please enter valid price")

    @property
    def thumbnail_url(self):
        return self.__thumbnail_url
