from config.Calculator import Calculator


class TestFurtherCalci():

    def test_modulus(self):
        x, y = 2, 2
        instance = Calculator(x, y)
        assert instance.modulus() == x % y, "Some issue in Modulus Method"

    def test_exponent(self):
        x, y = 2, 3
        instance = Calculator(x, y)
        assert instance.exponent() == 2 ^ 3, "Some issue in Exponent Method"
