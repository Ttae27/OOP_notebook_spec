class GPU:
    def __init__(self,
                id :int,
                series :str,
                model :str,
                chipset :str,
                clock :str,
                boost_clock :int,
                mem_speed :str,
                mem_size :str,
                bit :str,
                mem_type :str,
                bus_type :str,
                cf_sli :str,
                directx :int,
                opengl :float,
                shader :float,
                dsub :int,
                dvi :int,
                hdmi :int,
                hdmi_mini :int,
                displayport :int,
                displayport_mini :int,
                usbc :int,
                power :str,
                psu_require :str,
                warranty :int,
                brand_name :str,
                full_name :str,
                price :int,
                thumbnail_url :str
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
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price
