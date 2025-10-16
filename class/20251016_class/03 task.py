class Counter:
    def increment(self, start):
        self.start = start
        self.start += 1
        return self.start

    def value(self):
        return self.start

first_class = Counter()
second_operation = first_class.increment(10)
answer = first_class.value()
print(answer)