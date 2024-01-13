from messagesType import show_count
from pytest import mark

@mark.parametrize('qty, expected', [
    (1, '1 parts'),
    (2, '2 parts')
])

@mark.parametrize('zero, expected', [
    (0, '0 parts')    
])

def test_show_count(qty: int, expected: str) -> None:
    got = show_count(qty, 'part')
    assert got == expected

def test_show_count_zero(zero : int, expected: str) -> None:
    got = show_count(zero, 'part')
    assert got == expected

"""
1. mypy messagestype_test.py 
no errors

2. mypy --disallow-untyped-defs  messagestype_test.py
no errors
"""