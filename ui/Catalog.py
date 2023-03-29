class Catalog():
    def __init__(self, admin):
        # self.compatibility = compatibility
        self.admin_password = admin.password
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
        if self.is_admin():
            self.case.append(case)
            print(f"Successfully add {case}")
        else:
            print("Unauthorized: Admin password required")

    def add_cooling(self, cooling):
        if self.is_admin():
            self.cooling.append(cooling)
            print(f"Successfully add {cooling}")
        else:
            print("Unauthorized: Admin password required")

    def add_cpu(self, cpu):
        if self.is_admin():
            self.cpu.append(cpu)
            print(f"Successfully add {cpu}")
        else:
            print("Unauthorized: Admin password required")

    def add_gpu(self, gpu):
        if self.is_admin():
            self.gpu.append(gpu)
            print(f"Successfully add {gpu}")
        else:
            print("Unauthorized: Admin password required")

    def add_monitor(self, monitor):
        if self.is_admin():
            self.monitor.append(monitor)
            print(f"Successfully add {monitor}")
        else:
            print("Unauthorized: Admin password required")

    def add_motherboard(self, motherboard):
        if self.is_admin():
            self.motherboard.append(motherboard)
            print(f"Successfully add {motherboard}")
        else:
            print("Unauthorized: Admin password required")

    def add_psu(self, psu):
        if self.is_admin():
            self.psu.append(psu)
            print(f"Successfully add {psu}")
        else:
            print("Unauthorized: Admin password required")

    def add_ram(self, ram):
        if self.is_admin():
            self.ram.append(ram)
            print(f"Successfully add {ram}")
        else:
            print("Unauthorized: Admin password required")

    def add_storage(self, storage):
        if self.is_admin():
            self.storage.append(storage)
            print(f"Successfully add {storage}")
        else:
            print("Unauthorized: Admin password required")

    def remove_case(self, case):
        if self.is_admin():
            self.case.remove(case)
            print(f"Successfully remove {case}")
        else:
            print("Unauthorized: Admin password required")
    
    def remove_cooling(self, cooling):
        if self.is_admin():
            self.cooling.remove(cooling)
            print(f"Successfully remove {cooling}")
        else:
            print("Unauthorized: Admin password required")

    def remove_cpu(self, cpu):
        if self.is_admin():
            self.cpu.remove(cpu)
            print(f"Successfully remove {cpu}")
        else:
            print("Unauthorized: Admin password required")

    def remove_gpu(self, gpu):
        if self.is_admin():
            self.gpu.remove(gpu)
            print(f"Successfully remove {gpu}")
        else:
            print("Unauthorized: Admin password required")

    def remove_monitor(self, monitor):
        if self.is_admin():
            self.monitor.remove(monitor)
            print(f"Successfully remove {monitor}")
        else:
            print("Unauthorized: Admin password required")

    def remove_motherboard(self, motherboard):
        if self.is_admin():
            self.motherboard.remove(motherboard)
            print(f"Successfully remove {motherboard}")
        else:
            print("Unauthorized: Admin password required")

    def remove_psu(self, psu):
        if self.is_admin():
            self.psu.remove(psu)
            print(f"Successfully remove {psu}")
        else:
            print("Unauthorized: Admin password required")

    def remove_ram(self, ram):
        if self.is_admin():
            self.ram.remove(ram)
            print(f"Successfully remove {ram}")
        else:
            print("Unauthorized: Admin password required")

    def remove_storage(self, storage):
        if self.is_admin():
            self.storage.remove(storage)
            print(f"Successfully remove {storage}")
        else:
            print("Unauthorized: Admin password required")

    def is_admin(self):
        password = input("Enter admin password: ")
        return password == self.admin_password

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