from Calculator import Calculator

class TestCalci():

    def test_add(self):
        x, y = 1, 2
        instance = Calculator(x,y)
        assert instance.add() == x + y, "Some issue in Add Method"

    def test_substract(self):
        x, y = 2, 1
        instance = Calculator(x,y)
        assert instance.substract() == x - y, "Some issue in Substarct Method"