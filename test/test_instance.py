from pprint import pprint

class MyDictClass:
    def __init__(self, my_dict):
        for key, value in my_dict.items():
            setattr(self, f"__{key}", value)


x = MyDictClass({'hello':'World!'})


pprint(vars(MyDictClass))
attrs = dir(MyDictClass)

# print all attributes of the object
for attr in attrs:  # ignore special attributes
    print(attr, '=', getattr(MyDictClass, attr))