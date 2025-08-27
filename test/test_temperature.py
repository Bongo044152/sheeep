# file: tests/test_temperature.py

import pytest
from utils.temperature import c_to_f, f_to_c


def test_c_to_f():
    # 攝氏 0 度 = 華氏 32 度
    assert c_to_f(0) == pytest.approx(32.0)
    # 攝氏 100 度 = 華氏 212 度
    assert c_to_f(100) == pytest.approx(212.0)
    # 攝氏 -40 度 = 華氏 -40 度
    assert c_to_f(-40) == pytest.approx(-40.0)


def test_f_to_c():
    # 華氏 32 度 = 攝氏 0 度
    assert f_to_c(32) == pytest.approx(0.0)
    # 華氏 212 度 = 攝氏 100 度
    assert f_to_c(212) == pytest.approx(100.0)
    # 華氏 -40 度 = 攝氏 -40 度
    assert f_to_c(-40) == pytest.approx(-40.0)
