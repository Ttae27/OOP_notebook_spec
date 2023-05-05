class Monitor:
    def __init__(self,
                id: int,
                series: str,
                model: str,
                size: float,
                hdr_detail: int,
                reso: str,
                ratio: str,
                refresh_rate: int,
                response: str,
                bright: int,
                speaker: int,
                hdmi: int,
                displayport: int,
                mini_displayport: int,
                dvi: int,
                vga: int,
                tech_feature: int,
                flicker_free: int,
                warranty: int,
                brand_name: str,
                full_name: str,
                price: int,
                thumbnail_url: str,
                cont: str
                ):

        self.__id = id
        self.__series = series
        self.__model = model
        self.__size = size
        self.__hdr_detail = hdr_detail
        self.__reso = reso
        self.__ratio = ratio
        self.__refresh_rate = refresh_rate
        self.__response = response
        self.__bright = bright
        self.__speaker = speaker
        self.__hdmi = hdmi
        self.__displayport = displayport
        self.__mini_displayport = mini_displayport
        self.__dvi = dvi
        self.__vga = vga
        self.__tech_feature = tech_feature
        self.__flicker_free = flicker_free
        self.__warranty = warranty
        self.__brand_name = brand_name
        self.__full_name = full_name
        self.__price = price
        self.__thumbnail_url = thumbnail_url
        self.__cont = cont

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
    def size(self):
        return self.__size

    @property
    def hdr_detail(self):
        return self.__hdr_detail

    @property
    def reso(self):
        return self.__reso

    @property
    def ratio(self):
        return self.__ratio

    @property
    def refresh_rate(self):
        return self.__refresh_rate

    @property
    def response(self):
        return self.__response

    @property
    def bright(self):
        return self.__bright

    @property
    def speaker(self):
        return self.__speaker

    @property
    def hdmi(self):
        return self.__hdmi

    @property
    def displayport(self):
        return self.__displayport

    @property
    def mini_displayport(self):
        return self.__mini_displayport

    @property
    def dvi(self):
        return self.__dvi

    @property
    def vga(self):
        return self.__vga

    @property
    def tech_feature(self):
        return self.__tech_feature

    @property
    def flicker_free(self):
        return self.__flicker_free

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

    @property
    def cont(self):
        return self.__cont

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) and new_price > 0:
            self.__price = new_price
        else:
            print("Please enter valid price") #!need to change this