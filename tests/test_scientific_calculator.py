import math
import pytest

from scientific_calculator import ScientificCalculator

calc = ScientificCalculator()

def test_basic_operations():
    assert calc.add(2, 3) == 5
    assert calc.subtract(5, 2) == 3
    assert calc.multiply(4, 5) == 20
    assert calc.divide(10, 2) == 5

def test_power_and_sqrt():
    assert calc.power(2, 3) == 8
    assert calc.sqrt(16) == 4


def test_trig_and_log():
    assert math.isclose(calc.sin(math.pi / 2), 1.0)
    assert math.isclose(calc.cos(0), 1.0)
    assert math.isclose(calc.tan(math.pi / 4), 1.0)
    assert math.isclose(calc.log(math.e), 1.0)
    assert math.isclose(calc.log(8, 2), 3.0)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
