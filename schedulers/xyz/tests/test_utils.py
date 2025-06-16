# schedulers/xyz/tests/test_utils.py
import pytest
from schedulers.xyz.utils import greet

def test_greet_normal():
    assert greet("Alice") == "Hello, Alice!"

def test_greet_empty():
    with pytest.raises(ValueError):
        greet("")