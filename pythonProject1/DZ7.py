class number_range:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        for i in range(self.limit):
            yield i

numbers = number_range(10)
for num in numbers:
    print(num)