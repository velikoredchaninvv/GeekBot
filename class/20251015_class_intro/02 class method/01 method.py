# Следующая часть: методы в классах (кратко) — как создавать и возвращать результаты

# Метод экземпляра — обычная функция внутри класса, первый параметр обычно self. Используется для работы с состоянием конкретного объекта.
# Метод возвращает значение через return — это позволяет передавать результат дальше (между объектами/классами).
# @classmethod — принимает класс cls, полезен для фабрик/альтернативных конструкторов.
# @staticmethod — обычная функция в пространстве класса, не использует self или cls.

# The instance method that returns the value

class Coutner:
    def __init__(self):
        self.count = 0
    def increment(self, step=1):
        self.count += step * 4
        return self.count
    
obj = Coutner()
second_obj = obj.increment(2)
print(second_obj)