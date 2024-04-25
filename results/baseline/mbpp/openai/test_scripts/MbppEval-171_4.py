import math

def perimeter_pentagon(a):
    return a * 5

# Test cases




def check(candidate):
    assert perimeter_pentagon(5) == 25
    assert perimeter_pentagon(10) == 50
    assert perimeter_pentagon(15) == 75

check(perimeter_pentagon)