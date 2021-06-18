"""Unit tests for list utils in ls27."""
# python -m pytest lessons/ls27_list_utils_test.py
import pytest
from ls27_list_utils import max

def test_max_edge_case() -> None:
    """Testing max with empty list."""
    max([])

def test_max_1() -> None:
    """Test max with a single element."""
    assert max([110]) == 110

def test_max_2() -> None:
    """Test max with multiple elements."""
    assert max([1,5,2]) == 5

