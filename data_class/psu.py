class PSU:
    def __init__(self,
                id: int,
                series: str,
                model: str,
                form_factor: str,
                max_pw: str,
                modular: str,
                fans: str,
                certificates: str,
                efficiency: str,
                input_volt: str,
                input_frequency: str,
                dimension: str,
                main_connect: str,
                pci_ex: str,
                sata_connect: int,
                molex: str,
                warranty: int,
                brand_name: str,
                full_name: str,
                price: int,
                thumbnail_url: str
                ):

        self.__id = id
        self.__series = series
        self.__model = model
        self.__form_factor = form_factor
        self.__max_pw = max_pw
        self.__modular = modular
        self.__fans = fans
        self.__certificates = certificates
        self.__efficiency = efficiency
        self.__input_volt = input_volt
        self.__input_frequency = input_frequency
        self.__dimension = dimension
        self.__main_connect = main_connect
        self.__pci_ex = pci_ex
        self.__sata_connect = sata_connect
        self.__molex = molex
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
    def form_factor(self):
        return self.__form_factor

    @property
    def max_pw(self):
        return self.__max_pw

    @property
    def modular(self):
        return self.__modular

    @property
    def fans(self):
        return self.__fans

    @property
    def certificates(self):
        return self.__certificates

    @property
    def efficiency(self):
        return self.__efficiency

    @property
    def input_volt(self):
        return self.__input_volt

    @property
    def input_frequency(self):
        return self.__input_frequency

    @property
    def dimension(self):
        return self.__dimension

    @property
    def main_connect(self):
        return self.__main_connect

    @property
    def pci_ex(self):
        return self.__pci_ex

    @property
    def sata_connect(self):
        return self.__sata_connect

    @property
    def molex(self):
        return self.__molex

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