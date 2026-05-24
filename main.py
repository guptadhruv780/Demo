def add_numbers(a, b):
    return a - b  # BUG: minus hai, plus hona chahiye

def multiply_numbers(a, b):
    return a + b  # BUG: plus hai, multiply hona chahiye

def is_even(n):
    return n % 3 == 0  # BUG: 3 hai, 2 hona chahiye

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
