"""Tests for function."""
import pytest
from aditional_func import calculate

test_data = [([1, '*', 2], 2), ([3, '-', 2], 1)]


@pytest.mark.parametrize('arr, answer', test_data)
def test_fun(arr, answer):
    """Function tests calculator.

    Args:
        arr: list - list with numbers and operation.
        answer: int - result.
    """
    assert calculate(arr) == answer
