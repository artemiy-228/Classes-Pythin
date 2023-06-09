class Computation:

    def __init__(self):
        pass

    def factorial(self, num):
        f = 1
        for i in range(1, num + 1):
            f *= i
        return f

    def sum(self, num):
        return int(num * (num + 1) / 2)

    def test_prime(self, num):
        num = abs(num)
        if num <= 1:
            return False
        d = 2
        while(d * d <= num):
            if num % d == 0:
                return False
            d += 1
        return True

    def test_prims(self, a, b):
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        if a + b == 1:
            return True
        return False

    def table_mult(self, x):
        return [i * x for i in range(1, 11)]

    def all_table_mult(self):
        for i in range(11):
            yield [i * j for j in range(1, 11)]


Calculator = Computation()
print(Calculator.factorial(5))
print(Calculator.sum(5))
print(Calculator.test_prime(111))
print(Calculator.test_prims(121, 11))
print(Calculator.table_mult(5))
print(list(Calculator.all_table_mult()))

