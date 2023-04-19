class Case:
    def __init__(self, id: int, model: str, mat: str, color: str, weight: str, dimension: str, io: str, warranty: int, active: int, brand_name: str, full_name: str, price: int, thumbnail_url: str):
        self.__id = id
        self.__model = model
        self.__mat = mat
        self.__color = color
        self.__weight = weight
        self.__dimension = dimension
        self.__io = io
        self.__warranty = warranty
        self.__active = active
        self.__brand_name = brand_name
        self.__full_name = full_name
        self.__price = price 
        self.__thumbnail_url = thumbnail_url