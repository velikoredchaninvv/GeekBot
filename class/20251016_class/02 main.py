# Способ без сохранения в атрибуте аргумента
# Через передачу аргумента в параметр

class Calculator2:
    def add(self, a, b):
        return a+b
    
    def multiply(self, value, factor):
        return value * factor

c2 = Calculator2()
r = c2.add(10,5)
m = c2.multiply(r, 3)
print(r, m)

# использую атрибуты если состояние нужно сохранить между вызовами
# использую return + аргументы, если хочу чистые функции без побочных эффектов (удобнее для тестирования)