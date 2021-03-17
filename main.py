import unittest


class CalculatorTool:

    def __init__(self, **kwargs):
        self.first_num = int(kwargs.get("first_num")) or None
        self.second_num = int(kwargs.get("second_num")) or None
        self.symbol_of_action = kwargs.get("symbol_of_action") or None
        self.result = None

    def actions(self):
        if self.symbol_of_action == "+":
            self.result = \
                self.first_num + self.second_num
        elif self.symbol_of_action == "-":
            self.result = \
                self.first_num - self.second_num
        elif self.symbol_of_action == "*":
            self.result = \
                self.first_num * self.second_num
        elif self.symbol_of_action == "/":
            self.result = \
                self.first_num / self.second_num
        return self.result

    def print_result(self):
        self.result = int(self.result)
        print("Результат:", self.result)


# c = CalculatorTool(first_num="25", second_num="5", symbol_of_action="/")
# c.actions()
# c.print_result()

class TestCalculator(unittest.TestCase):

    def test_plus(self):
        pass

    def test_minus(self):
        pass

    def test_multiply(self):
        pass

    def test_divide(self):
        pass
