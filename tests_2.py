import pytest
import functions
from functions import *

# def test_method1 ():
#     x = 5
#     y = 10
#     assert x == y
#
# def test_method2 ():
#     a = 15
#     b = 20
#     assert a+5 == b
#
# def test_method3 ():
#     assert no_of_letters('12345678') == 8

# @pytest.fixture
#
# def numbers() :
#     a = 10
#     b = 20
#     c = 30
#     return [a,b,c]
#
# def test_method4 (numbers) :
#     assert numbers[0] == 10
# def test_method5 (numbers) :
#     assert numbers[1] == 15
# def test_method6 (numbers) :
#     assert numbers[2] == 30

@pytest.mark.parametrize ('x,y,z',[(10,20,200), (20,40,200)])
def test1(x,y,z):
    assert x*y == z