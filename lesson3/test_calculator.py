import random

import pytest
from calculator import CalculatorFunctions


class TestCalculator(CalculatorFunctions):

    @pytest.mark.parametrize(
        "number_1, number_2, expected_result", [
            (1, 2, 3),
            (-1, 1, 0),
            (-1, -1, -2),
            (0, 0, 0),
            (1.5, 2.5, 4.0)
        ])
    def test_calc_summa(self, number_1, number_2, expected_result):
        result = self.summa(number_1, number_2)
        assert expected_result == result

    @pytest.mark.parametrize(
        "number_1, number_2, expected_result", [
            (5, 2, 3),
            (-1, 1, -2),
            (-1, -1, 0),
            (0, 0, 0),
            (1.5, 2.5, -1.0)
        ])
    def test_calc_raznost(self, number_1, number_2, expected_result):
        result = self.raznost(number_1, number_2)
        assert expected_result == result

    @pytest.mark.parametrize(
        "number_1, number_2, expected_result", [
            (5, 2, 10),
            (-1, 1, -1),
            (-1, -1, 1),
            (0, 5, 0),
            (1.5, 2.5, 3.75)
        ])
    def test_calc_umnojenie(self, number_1, number_2, expected_result):
        result = self.umnojenie(number_1, number_2)
        assert expected_result == result

    @pytest.mark.parametrize(
        "number_1, number_2, expected_result", [
            (6, 2, 3.0),
            (-1, 1, -1.0),
            (-1, -1, 1.0),
            (0, 5, 0.0),
            (5,0, None),
            (1.5, 2.5, 0.6)
        ])
    def test_calc_delenie(self, number_1, number_2, expected_result):
        if expected_result is None:
            print("Деление на НОЛЬ")
        else:
            result = self.delenie(number_1, number_2)
            assert expected_result == result
