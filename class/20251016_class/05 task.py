class Generator:
    def generate(self):
        return 10
    
class Consumer:
    def __init__(self, generator):
        self.generator = generator

    def process(self):
        result = self.generator.generate()
        return result * 2
    
g = Generator()
c = Consumer(g)
print(c.process())