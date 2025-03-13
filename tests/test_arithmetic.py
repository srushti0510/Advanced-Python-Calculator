import pytest # type: ignore
from app.arithmetic import add, subtract, multiply, divide

def test_add():
    # Test positive numbers
    assert add(2, 3) == 5
    # Test negative numbers
    assert add(-2, -3) == -5
    # Test with zero
    assert add(0, 5) == 5
    # Test with floats
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    # Test basic subtraction
    assert subtract(5, 3) == 2
    # Test negative result
    assert subtract(3, 5) == -2
    # Test with zero
    assert subtract(5, 0) == 5
    # Test with floats
    assert subtract(5.5, 3.2) == pytest.approx(2.3)

def test_multiply():
    # Test basic multiplication
    assert multiply(2, 3) == 6
    # Test with zero
    assert multiply(5, 0) == 0
    # Test with negative numbers
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    # Test with floats
    assert multiply(2.5, 2) == 5.0

def test_divide():
    # Test basic division
    assert divide(6, 3) == 2
    # Test division with floats
    assert divide(5, 2) == 2.5
    # Test division with negative numbers
    assert divide(-6, 3) == -2
    assert divide(6, -3) == -2
    assert divide(-6, -3) == 2

def test_divide_by_zero():
    # Test division by zero raises ValueError
    with pytest.raises(ValueError):
        divide(5, 0)