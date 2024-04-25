def square_Sum(n):
    if n <= 0:
        return 0
    else:
        return sum([x**2 for x in range(2, 2*n+1, 2)])

# Test the function




def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)