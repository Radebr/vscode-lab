import pytest
from sum_positive import sum_positive

def test_sum_positive_normal():
    assert sum_positive([1, 2, 3]) == 6

def test_sum_positive_empty():
    assert sum_positive([]) == 0

def test_sum_positive_single():
    assert sum_positive([10]) == 10

def test_sum_positive_with_negative():
    with pytest.raises(ValueError):
        sum_positive([1, -2, 3])
