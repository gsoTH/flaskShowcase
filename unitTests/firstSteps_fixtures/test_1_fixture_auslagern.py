import pytest

## In conftest.py ausgelagert:
# @pytest.fixture
# def input_value():
#    input = 39
#    return input

def test_divisible_by_3(input_value):     # input_value ist der Return-Wert der gleichnamigen Methode
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0