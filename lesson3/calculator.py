from logging import raiseExceptions


class CalculatorFunctions:

    def summa(self, number_1: int, number_2: int) -> int:
        return number_1 + number_2

    def raznost(self, number_1: int, number_2: int) -> int:
        return number_1 - number_2

    def umnojenie(self, number_1: int, number_2: int) -> int:
        return number_1 * number_2

    def delenie(self, number_1: int, number_2: int) -> float:
        if number_2 == 0:
            return None
        return number_1 / number_2
