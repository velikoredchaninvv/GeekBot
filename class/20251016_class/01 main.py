# План урока

# Основы: класс, атрибуты, методы, return и хранение результата в атрибуте. 🟢  
# Передача данных между методами одного класса (возврат vs состояние объекта). 🔵  
# Передача данных между разными классами (композиция, передача экземпляра/результата). 🟠  
# Практический пример: вычисления в одном классе → использование в другом. 🟣

# Собсоб - вычисление и сохранение результата в атрибуте и дальнейший возврат
class Calculator:
    def __init__(self, base):
        self.base = base # атрибут экземляра
        self.last = None # сюда можно сохранять результат

    def add(self, x):
        result = self.base + x
        self.last = result # сохраняем в атрибут
        return result # и одновременно возвращаем
    
    def multiply_using_last(self, factor):
        # читаем ранее сохранённый результат из self.last
        if self.last is None:
            raise ValueError('Нет сохранённого результата')
        return self.last * factor
    
# Использование
c = Calculator(10)
r = c.add(5)
m = c.multiply_using_last(3)
print(r, m)

