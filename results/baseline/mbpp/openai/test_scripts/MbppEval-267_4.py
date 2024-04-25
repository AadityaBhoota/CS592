def square_Sum(n):
    sum = 0
    for i in range(1, 2 * n + 1, 2):
        sum += i * i
    return sum

# Test cases




def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)