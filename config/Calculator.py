class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def minus(self):
        if self.num1 > self.num2:
            return self.num1 - self.num2
        else:
            return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def modulus(self):
        return self.num1 % self.num2

    def exponent(self):
        return self.num1 ^ self.num2


if __name__ == '__main__':
    instance = Calculator(1, 2)
    print(instance.add())
