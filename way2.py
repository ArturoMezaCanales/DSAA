class FibonacciIterator:
    def __init__(self, n):
        self.n = n  # how many Fibonacci numbers to generate
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.n:
            raise StopIteration
        
        if self.index == 0:
            self.index += 1
            return 0
        elif self.index == 1:
            self.index += 1
            return 1
        else:
            next_val = self.a + self.b
            self.a, self.b = self.b, next_val
            self.index += 1
            return next_val
        
fib = FibonacciIterator(10)

for num in fib:
    print(num)