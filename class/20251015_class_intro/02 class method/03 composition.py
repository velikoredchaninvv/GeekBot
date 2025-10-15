# Transfer the result between classes

class Engine:
    def power(self):
        return 150
    
class Car:
    def __init__(self, engine):
        self.engine = engine

    def engine_power(self):
        return self.engine.power() # вызываем метод другого объекта и возвращаем результат
    
engine = Engine()
variant = Car(engine)

sec_variant = variant.engine_power()
print(sec_variant)