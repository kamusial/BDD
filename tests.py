# import pytest
from functions import *


def test_0():
    assert add(5, 3) == 8


def test_1():
    assert no_of_letters('Takieslowo') == 10


def test_2():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == "4"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
    assert fizzbuzz(1800) == "FizzBuzz"
    assert fizzbuzz(66) == "Fizz"
    assert fizzbuzz(69) == "Fizz"
    assert fizzbuzz(72) == "Fizz"
    assert fizzbuzz(16) == "16"
    assert fizzbuzz(1234) == "1234"

# @pytest.mark.parametrize('x',[1,5,10,21])
# def test_2 (x):
#     assert fizzbuzz(x) == str(x)

def test_4():
   assert playfizzbuzz(3) == 3
   assert playfizzbuzz('mama') == None
   assert playfizzbuzz(0) == None
   assert playfizzbuzz(5) == 5
   assert playfizzbuzz(12) == 12

def test_5():
   assert ileosob(100, True) == 110
   assert ileosob(100, False) == 50
   assert ileosob(97, True) == 106
   assert ileosob(97, False) == 48
   assert ileosob(10.4, True) == None
   assert ileosob('mama', 50) == None
   assert ileosob(-17, True) == None
   assert ileosob(False, True) == None
   assert ileosob(1, True) == 1
   assert ileosob(1, False) == 1
   assert ileosob(0, True) == None

