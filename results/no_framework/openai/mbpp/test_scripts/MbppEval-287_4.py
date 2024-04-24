def square_Sum(n):
    sum = 0
    for i in range(1, 2*n+1):
        if i % 2 == 0:
            sum += i**2
    return sum

# Test cases




def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)