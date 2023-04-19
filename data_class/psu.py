class PSU:
    def __init__(self,
                id :int,
                series :str,
                model :str,
                form_factor :str,
                max_pw :str,
                modular :str,
                fans :str,
                certificates :str,
                efficiency :str,
                input_volt :str,
                input_frequency :str,
                dimension :str,
                main_connect :str,
                pci_ex :str,
                sata_connect :int,
                molex :str,
                warranty :int,
                brand_name :str,
                full_name :str,
                price :int,
                thumbnail_url :str
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
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price