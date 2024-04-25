def maximum(a, b):
    return a if a > b else b

# Test the function




def check(candidate):
    assert maximum(5,10) == 10
    assert maximum(-1,-2) == -1
    assert maximum(9,7) == 9

check(maximum)