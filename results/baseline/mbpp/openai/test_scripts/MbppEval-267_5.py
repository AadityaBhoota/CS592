def square_Sum(n):
    return sum([(2*i-1)**2 for i in range(1, n+1)])

# Test cases




def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)