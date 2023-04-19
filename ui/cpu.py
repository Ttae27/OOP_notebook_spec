class CPU:
    def __init__(self, series: str, model: str, socket: str, chipsupport: str, core:int, thread:int, frequency:str, l2:str, l3:str, gpu_integrated:str, power:str, warranty:int, active:int, brand_name:str, full_name:str, price:int, thumbnail_url:str):
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