class Monitor:
    def __init__(self,
                id :int,
                series :str,
                model :str,
                size :float,
                hdr_detail :int,
                reso :str,
                ratio :str,
                refresh_rate :int,
                response :str,
                bright :int,
                speaker :int,
                hdmi :int,
                displayport :int,
                mini_displayport :int,
                dvi :int,
                vga :int,
                tech_feature :int,
                flicker_free :int,
                warranty :int,
                brand_name :str,
                full_name :str,
                price :int,
                thumbnail_url :str,
                cont :str
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
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price