def square_Sum(n):
    sum = 0
    num = 1
    for i in range(n):
        sum += num ** 2
        num += 2
    return sum

# Test cases




def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)