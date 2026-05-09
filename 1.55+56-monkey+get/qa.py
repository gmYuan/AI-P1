

# -----------------------------------------------------------------------------

class Cat:
    pass


def meow(self):
    return f"{self.name} 喵喵..."


Cat.speak = meow
cat1 = Cat()
cat1.name = "小白"
print(cat1.speak())