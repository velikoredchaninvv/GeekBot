# Разобьём тему на части — так будет проще учиться:

# Основы классов и объектов — объявление класса, __init__, атрибуты, создание экземпляра.  
# Методы — обычные методы экземпляра, @classmethod, @staticmethod, использование self.  
# Передача результатов между классами — возвращаемые значения, композиция/агрегация, передача объектов/результатов как аргументов.  
# Практические шаблоны — фабрики, сервисы, обработчики, примеры взаимодействия.

class Human:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

obj_slava = Human('Slava', 49, 'Moscow')
print(obj_slava.name)
print(obj_slava.age)
print(obj_slava.city)