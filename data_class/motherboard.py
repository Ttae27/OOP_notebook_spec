class Motherboard:
    def __init__(self,
                id: int,
                chipset: str,
                model: str,
                socket: str,
                cpu_list: str,
                mem_slot: int,
                mem_max: int,
                mem_type: str,
                mem_bus: str,
                gpu_chip: str,
                audio_chip: str,
                audio_chan: str,
                lan_chip: str,
                lan_speed: str,
                lan_wireless: str,
                bluetooth: str,
                pcie_slot: int,
                pci_slot: int,
                gpu_multi: int,
                sata2: int,
                sata3: int,
                m2_slot: int,
                m2_type: str,
                raid: str,
                usb2: int,
                usb3: int,
                usb31a: int,
                usb31c: int,
                usb32a: str,
                usb32c: str,
                hdmi: int,
                hdmi_mini: int,
                displayport: int,
                displayport_mini: int,
                dvi: int,
                vga: int,
                audio: int,
                ps2: int,
                factor: str,
                pw_pin: str,
                dimension: str,
                warranty: int,
                brand_name: str,
                full_name: str,
                price: int,
                thumbnail_url: str
                ):

        self.__id = id
        self.__chipset = chipset
        self.__model = model
        self.__socket = socket
        self.__cpu_list = cpu_list
        self.__mem_slot = mem_slot
        self.__mem_max = mem_max
        self.__mem_type = mem_type
        self.__mem_bus = mem_bus
        self.__gpu_chip = gpu_chip
        self.__audio_chip = audio_chip
        self.__audio_chan = audio_chan
        self.__lan_chip = lan_chip
        self.__lan_speed = lan_speed
        self.__lan_wireless = lan_wireless
        self.__bluetooth = bluetooth
        self.__pcie_slot = pcie_slot
        self.__pci_slot = pci_slot
        self.__gpu_multi = gpu_multi
        self.__sata2 = sata2
        self.__sata3 = sata3
        self.__m2_slot = m2_slot
        self.__m2_type = m2_type
        self.__raid = raid
        self.__usb2 = usb2
        self.__usb3 = usb3
        self.__usb31a = usb31a
        self.__usb31c = usb31c
        self.__usb32a = usb32a
        self.__usb32c = usb32c
        self.__hdmi = hdmi
        self.__hdmi_mini = hdmi_mini
        self.__displayport = displayport
        self.__displayport_mini = displayport_mini
        self.__dvi = dvi
        self.__vga = vga
        self.__audio = audio
        self.__ps2 = ps2
        self.__factor = factor
        self.__pw_pin = pw_pin
        self.__dimension = dimension
        self.__warranty = warranty
        self.__brand_name = brand_name
        self.__full_name = full_name
        self.__price = price
        self.__thumbnail_url = thumbnail_url

    @property
    def id(self):
        return self.__id

    @property
    def chipset(self):
        return self.__chipset

    @property
    def model(self):
        return self.__model

    @property
    def socket(self):
        return self.__socket

    @property
    def cpu_list(self):
        return self.__cpu_list

    @property
    def mem_slot(self):
        return self.__mem_slot

    @property
    def mem_max(self):
        return self.__mem_max

    @property
    def mem_type(self):
        return self.__mem_type

    @property
    def mem_bus(self):
        return self.__mem_bus

    @property
    def gpu_chip(self):
        return self.__gpu_chip

    @property
    def audio_chip(self):
        return self.__audio_chip

    @property
    def audio_chan(self):
        return self.__audio_chan

    @property
    def lan_chip(self):
        return self.__lan_chip

    @property
    def lan_speed(self):
        return self.__lan_speed

    @property
    def lan_wireless(self):
        return self.__lan_wireless

    @property
    def bluetooth(self):
        return self.__bluetooth

    @property
    def pcie_slot(self):
        return self.__pcie_slot

    @property
    def pci_slot(self):
        return self.__pci_slot

    @property
    def gpu_multi(self):
        return self.__gpu_multi

    @property
    def sata2(self):
        return self.__sata2

    @property
    def sata3(self):
        return self.__sata3

    @property
    def m2_slot(self):
        return self.__m2_slot

    @property
    def m2_type(self):
        return self.__m2_type

    @property
    def raid(self):
        return self.__raid

    @property
    def usb2(self):
        return self.__usb2

    @property
    def usb3(self):
        return self.__usb3

    @property
    def usb31a(self):
        return self.__usb31a

    @property
    def usb31c(self):
        return self.__usb31c

    @property
    def usb32a(self):
        return self.__usb32a

    @property
    def usb32c(self):
        return self.__usb32c

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
    def dvi(self):
        return self.__dvi

    @property
    def vga(self):
        return self.__vga

    @property
    def audio(self):
        return self.__audio

    @property
    def ps2(self):
        return self.__ps2

    @property
    def factor(self):
        return self.__factor

    @property
    def pw_pin(self):
        return self.__pw_pin

    @property
    def dimension(self):
        return self.__dimension

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