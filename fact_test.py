from math import factorial
import pytest


def test_fact_zero():
    assert factorial(0) == 1

def test_fact_one():
    assert factorial(1) == 1

def test_fact_two():
    assert factorial(2) == 2

def test_fact_three():
    assert factorial(3) == 6

def test_fact_five():
    assert factorial(5) == 120

def test_fact_ten():
    assert factorial(10) == 3628800

def test_fact_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_fact_large():
    assert factorial(12) == 479001600

def test_fact_small_positive():
    assert factorial(4) == 24

def test_fact_medium_positive():
    assert factorial(8) == 40320