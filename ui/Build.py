class Build:
    def __init__(self) -> None:
        self.__build = []

    def add_to_build(self, product):
        self.__build.append(product)

    @property
    def build(self):
        return self.__build

