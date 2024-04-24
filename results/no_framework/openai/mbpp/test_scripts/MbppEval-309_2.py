def maximum(a, b):
    # Compare the two numbers and return the maximum
    return a if a > b else b

# Test the function with the provided examples




def check(candidate):
    assert maximum(5,10) == 10
    assert maximum(-1,-2) == -1
    assert maximum(9,7) == 9

check(maximum)