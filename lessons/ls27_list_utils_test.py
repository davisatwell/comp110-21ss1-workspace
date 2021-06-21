"""Unit tests for list utils in ls27."""
# python -m pytest lessons/ls27_list_utils_test.py
import pytest
from ls27_list_utils import max, concat

def test_max_edge_case() -> None:
    """Testing max with empty list."""
    with pytest.raises(ValueError):
        max([])

def test_max_1() -> None:
    """Test max with a single element."""
    assert max([110]) == 110

def test_max_2() -> None:
    """Test max with multiple elements."""
    assert max([1,5,2]) == 5


def test_concat_use_1() -> None:
    """Test concat with 1 elt each."""
    assert concat([1],[2]) == [1,2]


def test_concat_use_2() -> None:
    """Another use case for concat."""
    assert concat([1,2,3],[2, 5]) == [1,2,3,2,5]


def test_concat_edge_1() -> None:
    """Testing concat with an empty a list."""
    assert concat([],[1,2,3]) == [1,2,3]


def test_concat_edge_2() -> None:
    """Testing concat with an empty b list."""
    assert concat([2,3],[]) == [2,3]


def test_concat_edge_3() -> None:
    """Testing concat with a and b as empty lists."""
    assert concat([],[]) == []