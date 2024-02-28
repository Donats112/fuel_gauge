from ..fuel import gauge, convert
import pytest

def test_convert():
    assert convert("1/2") == (1, 2)
    assert convert("0/2") == (0, 2)
    assert convert("-1/2") == (-1, 2)
    assert convert("1/0") == (1, 0)
    assert convert("0/0") == (0, 0)

def test_normal():
    assert gauge(1, 4) == "25.00%"
    assert gauge(1, 10) == "10.00%"
    assert gauge(2, 4) == "50.00%"
    assert gauge(69, 100) == "69.00%"
    assert gauge(2, 3) == "66.67%"

def test_F_E():
    assert gauge(4, 4) == "F"
    assert gauge(99, 100 ) == "F"
    assert gauge(0, 4) == "E"
    assert gauge(1, 100) == "E"
    assert gauge(1, 200) == "E"
    assert gauge(999, 1000) == "F"

def test_errors():
    with pytest.raises(ValueError):
        assert gauge(2, 1) is ValueError
    with pytest.raises(ValueError):
        assert gauge(4, 3) is ValueError
    with pytest.raises(ValueError):
        assert gauge(100, 69) is ValueError
    with pytest.raises(ZeroDivisionError):
        assert gauge(5, 0) is ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        assert gauge(0, 0) is ZeroDivisionError


test_normal()
test_F_E()
test_errors()