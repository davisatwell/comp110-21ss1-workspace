"""Unit tests for functions defined in 6/14's class."""

from exercises.ex14.list_utils import max, concat, all, sub
import pytest

__author__ = "730384155"


def test_example() -> None:
    """2 + 2 = 4."""
    assert 2 + 2 == 4


def test_max_edge_case() -> None:
    """Testing max with empty list."""
    with pytest.raises(ValueError):
        max([])


def test_max_1() -> None:
    """Test max with a single element."""
    assert max([110]) == 110


def test_max_2() -> None:
    """Test max with multiple elements."""
    assert max([1, 5, 2]) == 5


def test_concat_use_1() -> None:
    """Test concat with 1 elt each."""
    assert concat([1], [2]) == [1, 2]


def test_concat_use_2() -> None:
    """Another use case for concat."""
    assert concat([1, 2, 3], [2, 5]) == [1, 2, 3, 2, 5]


def test_concat_edge_1() -> None:
    """Testing concat with an empty a list."""
    assert concat([], [1, 2, 3]) == [1, 2, 3]


def test_concat_edge_2() -> None:
    """Testing concat with an empty b list."""
    assert concat([2, 3], []) == [2, 3]


def test_concat_edge_3() -> None:
    """Testing concat with a and b as empty lists."""
    assert concat([], []) == []


def test_all_use_1() -> None:
    """Testing all with desired True expression."""
    assert all([2, 2, 2, 2], 2) == True


def test_all_use_2() -> None:
    """Testing all with desired False expression."""
    assert all([1, 2, 1, 1], 1) == False


def test_all_edge_1() -> None:
    """Testing all edge case with empty xs list."""
    assert all([], 3) == False


def test_sub_use_1() -> None:
    """Testing sub with all parameters met."""
    assert sub([5, 6, 7, 8], 2, 4) == [7, 8]


def test_sub_use_2() -> None:
    """Testing sub with out of range stop value."""
    assert sub([1, 2, 3, 4], 0, 17) == [1, 2, 3]


def test_sub_edge_1() -> None:
    """Testing sub when a is empty."""
    assert sub([], 3, 5) == []