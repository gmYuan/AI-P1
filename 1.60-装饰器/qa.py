

# -----------------------------------------------------------------------------


class Person:
    def __call__(self, *args, **kwargs):
        print("实现了这个魔术方法，这个类的实例就可以当方法来调用")


person = Person()

# TypeError: 'Person' object is not callable
person()
