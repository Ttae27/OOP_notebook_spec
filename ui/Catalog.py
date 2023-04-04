class Catalog():
    def __init__(self):
        # self.compatibility = compatibility
        self.case = []
        self.cooling = []
        self.cpu = []
        self.gpu = []
        self.monitor = []
        self.motherboard = []
        self.psu = []
        self.ram = []
        self.storage = []

    def add_case(self, case):
        self.case.append(case)

    def add_cooling(self, cooling):
        self.cooling.append(cooling)

    def add_cpu(self, cpu):
        self.cpu.append(cpu)

    def add_gpu(self, gpu):
        self.gpu.append(gpu)

    def add_monitor(self, monitor):
        self.monitor.append(monitor)

    def add_motherboard(self, motherboard):
        self.motherboard.append(motherboard)

    def add_psu(self, psu):
        self.psu.append(psu)

    def add_ram(self, ram):
        self.ram.append(ram)

    def add_storage(self, storage):
        self.storage.append(storage)

    def list_case(self):
        for case in self.case:
            print(case)

    def list_cooling(self):
        for cooling in self.cooling:
            print(cooling)

    def list_cpu(self):
        for cpu in self.cpu:
            print(cpu)

    def list_gpu(self):
        for gpu in self.gpu:
            print(gpu)

    def list_monitor(self):
        for monitor in self.monitor:
            print(monitor)

    def list_motherboard(self):
        for motherboard in self.motherboard:
            print(motherboard)

    def list_psu(self):
        for psu in self.psu:
            print(psu)

    def list_ram(self):
        for ram in self.ram:
            print(ram)

    def list_storage(self):
        for storage in self.storage:
            print(storage)

    def get_item(self, name):
        for case in self.case:
            if case.model == name.model:
                return case
        for cooling in self.cooling:
            if cooling.model == name.model:
                return cooling
        for cpu in self.cpu:
            if cpu.model == name.model:
                return cpu
        for gpu in self.gpu:
            if gpu.model == name.model:
                return gpu
        for monitor in self.monitor:
            if monitor.model == name.model:
                return monitor
        for motherboard in self.motherboard:
            if motherboard.model == name.model:
                return motherboard
        for psu in self.psu:
            if psu.model == name.model:
                return psu
        for ram in self.ram:
            if ram.model == name.model:
                return ram
        for storage in self.storage:
            if storage.model == name.model:
                return storage
        return None

    def display():
        pass

    def search():
        pass

    def sort():
        pass

    def filter():
        pass