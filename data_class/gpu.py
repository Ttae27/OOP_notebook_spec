class GPU:
    def __init__(self, id, series, model, chipset, clock, boost_clock, mem_speed, mem_size, bit, mem_type, bus_type, cf_sli, directx, opengl, shader, dsub, dvi, hdmi, hdmi_mini, displayport, displayport_mini, usbc, power, psu_require, warranty, brand_name, full_name, price, thumbnail_url):
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
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price