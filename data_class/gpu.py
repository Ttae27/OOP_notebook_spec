class GPU:
    def __init__(self,
                id: int,
                series: str,
                model: str,
                chipset: str,
                clock: str,
                boost_clock: int,
                mem_speed: str,
                mem_size: str,
                bit: str,
                mem_type: str,
                bus_type: str,
                cf_sli: str,
                directx: int,
                opengl: float,
                shader: float,
                dsub: int,
                dvi: int,
                hdmi: int,
                hdmi_mini: int,
                displayport: int,
                displayport_mini: int,
                usbc: int,
                power: str,
                psu_require: str,
                warranty: int,
                brand_name: str,
                full_name: str,
                price: int,
                thumbnail_url: str
                ):

        self.__id = id
        self.__series = series
        self.__model = model
        self.__chipset = chipset
        self.__clock = clock
        self.__boost_clock = boost_clock
        self.__mem_speed = mem_speed
        self.__mem_size = mem_size
        self.__bit = bit
        self.__mem_type = mem_type
        self.__bus_type = bus_type
        self.__cf_sli = cf_sli
        self.__directx = directx
        self.__opengl = opengl
        self.__shader = shader
        self.__dsub = dsub
        self.__dvi = dvi
        self.__hdmi = hdmi
        self.__hdmi_mini = hdmi_mini
        self.__displayport = displayport
        self.__displayport_mini = displayport_mini
        self.__usbc = usbc
        self.__power = power
        self.__psu_require = psu_require
        self.__warranty = warranty
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
    def chipset(self):
        return self.__chipset

    @property
    def clock(self):
        return self.__clock

    @property
    def boost_clock(self):
        return self.__boost_clock

    @property
    def mem_speed(self):
        return self.__mem_speed

    @property
    def mem_size(self):
        return self.__mem_size

    @property
    def bit(self):
        return self.__bit

    @property
    def mem_type(self):
        return self.__mem_type

    @property
    def bus_type(self):
        return self.__bus_type

    @property
    def cf_sli(self):
        return self.__cf_sli

    @property
    def directx(self):
        return self.__directx

    @property
    def opengl(self):
        return self.__opengl

    @property
    def shader(self):
        return self.__shader

    @property
    def dsub(self):
        return self.__dsub

    @property
    def dvi(self):
        return self.__dvi

    @property
    def hdmi(self):
        return self.__hdmi

    @property
    def hdmi_mini(self):
        return self.__hdmi_mini

    @property
    def displayport(self):
        return self.__displayport

    @property
    def displayport_mini(self):
        return self.__displayport_mini

    @property
    def usbc(self):
        return self.__usbc

    @property
    def power(self):
        return self.__power

    @property
    def psu_require(self):
        return self.__psu_require

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