import pytest
import package as pack

def test_increment_int():
    assert pack.increment(3) == 4
    assert pack.increment(7) == 8

def test_increment_neg_int():
    assert pack.increment(-5) == -4

def test_increment_float():
    assert pack.increment(5.5) == 6.5