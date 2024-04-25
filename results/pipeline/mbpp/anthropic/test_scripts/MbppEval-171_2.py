import math

def perimeter_pentagon(a):
    perimeter = a * 5
    return perimeter

def check(candidate):
    assert perimeter_pentagon(5) == 25
    assert perimeter_pentagon(10) == 50
    assert perimeter_pentagon(15) == 75

check(perimeter_pentagon)