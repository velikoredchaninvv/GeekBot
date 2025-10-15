class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        x = f'Приветствую {self.name} c тем что тебе всего {self.age} лет!'
        return x

slava = Person('Slava', 40)
hi_slava = slava.greet()
print(hi_slava)