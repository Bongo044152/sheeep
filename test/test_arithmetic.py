# file: tests/test_arithmetic.py

import pytest
from utils.arithmetic import add, sub, mul, div


def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0


def test_sub():
    assert sub(10, 4) == 6
    assert sub(0, 7) == -7


def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 5) == -10


def test_div_normal():
    assert div(10, 2) == 5
    assert div(7, -1) == -7


def test_div_zero():
    with pytest.raises(ValueError) as excinfo:
        div(5, 0)
    assert "division by zero" in str(excinfo.value)
