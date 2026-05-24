from main import add_numbers, multiply_numbers, is_even, factorial

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0

def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(2, 2) == 4

def test_is_even():
    assert is_even(4) == True
    assert is_even(3) == False
    assert is_even(0) == True

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(3) == 6
