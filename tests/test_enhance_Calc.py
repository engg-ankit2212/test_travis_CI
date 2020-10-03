from config.Calculator import Calculator


class TestEnhanceCalci():

    def test_multiply(self):
        x, y = 1, 2
        instance = Calculator(x, y)
        assert instance.multiply() == x * y, "Some issue in Multiply Method"

    def test_divide(self):
        x, y = 2, 1
        instance = Calculator(x, y)
        assert instance.divide() == x / y, "Some issue in Divide Method"
