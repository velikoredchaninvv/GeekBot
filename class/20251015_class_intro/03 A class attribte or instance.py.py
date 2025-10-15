class Primer:
    class_attr = 'Общий для всех атрибут' # это атрибут класса
    def __init__(self, name):
        self.name = name # это атрибут экземляра

myprim = Primer('name')
print(myprim.name) 