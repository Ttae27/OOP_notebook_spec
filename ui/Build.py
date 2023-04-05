class Build():
    def __init__(self):
        self.build = {}
        self.show_build = {}
        self.totalPrice = 0

    def add_item(self, item):
        # if item in self.build[type(item).__name__]:
            self.build[type(item).__name__] = item
            self.show_build[type(item).__name__] = item.model

    def remove_item(self, item):
        self.build.pop(type(item).__name__)
        self.show_build.pop(type(item).__name__)

    def view(self):
        if len(self.build) == 0:
            print("Build is empty")
        else:
            for product in self.build.values():
                self.totalPrice += int(product.price)
            print(self.show_build)
            print(f"Total price = {self.totalPrice}")

    def check_compatibility():
        pass

    def reset():
        pass