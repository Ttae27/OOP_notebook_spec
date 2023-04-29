class Compare():
    def __init__(self):
        self.__spec_1 = []
        self.__spec_2 = []
        
    def add_item(self, item, i):
        if i == 1:
            if len(self.__spec_1) == 0:
                self.__spec_1.append(item)
                return {'Data': 'Successfully add item 1'}
        else:
            if len(self.__spec_2) == 0:
                self.__spec_2.append(item)
                return {'Data': 'Successfully add item 2'}
        return {'Data': 'Fail to add item ' + str(i)}
        
    def remove_item(self, i):
        if i == 1:
            self.__spec_1.clear()
        else:
            self.__spec_2.clear()
        return {'Data': 'Successfully remove item ' + str(i)}
        
    def compare_spec(self):
        if len(self.__spec_1) == 0 or len(self.__spec_2) == 0:
            return {'warning': 'please select product to compare!'}
        if type(self.__spec_1[0]).__name__ != type(self.__spec_2[0]).__name__:
            return {'warning': 'please select from same catalog!'}
        lst = [self.__spec_1[0], self.__spec_2[0]]
        return lst