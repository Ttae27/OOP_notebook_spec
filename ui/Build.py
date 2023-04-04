class Build():
    def __init__(self):
        self.build = {}
        self.totalPrice = 0

    def add_item(self, item):
        self.build[type(item).__name__] = item.model
        self.totalPrice += int(item.price)

    def remove_item(self, item):
        self.items.remove(item)
        self.totalPrice -= int(item.price)

    def view(self):
        if len(self.build) == 0:
            print("Build is empty")
        else:
            print(self.build)
            print(f"Total price = {self.totalPrice}")

    def check_compatibility():
        pass

    def reset():
        pass