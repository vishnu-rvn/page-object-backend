class Model:
    def __init__(self):
        pass

    def __getattr__(self, attr):
        pass


class Object:
    def __init__(self, attr_one=None, attr_two=None):
        self.attr_one = attr_one
        self.attr_two = attr_two


o = Object()
print(o.attr_one)