class Motherboard:
    def __init__(self, id, chipset, model, socket, cpu_list, mem_slot, mem_max, mem_type, mem_bus, gpu_chip, audio_chip, audio_chan, lan_chip, lan_speed, lan_wireless, bluetooth, pcie_slot, pci_slot, gpu_multi, sata2, sata3, m2_slot, m2_type, raid, usb2, usb3, usb31a, usb31c, usb32a, usb32c, hdmi, hdmi_mini, displayport, displayport_mini, dvi, vga, audio, ps2, factor, pw_pin, dimension, warranty, brand_name, full_name, price, thumbnail_url):
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
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price