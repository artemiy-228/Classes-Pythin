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


Calculator = Computation()
print(Calculator.factorial(5))
print(Calculator.sum(5))
print(Calculator.test_prime(111))