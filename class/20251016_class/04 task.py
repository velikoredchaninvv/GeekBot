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
    
    def subtract_and_store(self, x):
        self.x = x
        self.last = self.base - self.x
        return self.last
    
# Использование
c = Calculator(10)
r = c.add(5)
m = c.multiply_using_last(3)
h = c.subtract_and_store(2)
print(r, m, h)