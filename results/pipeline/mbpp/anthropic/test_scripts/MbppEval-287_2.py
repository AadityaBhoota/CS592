def square_Sum(n):
    total_sum = 0
    for i in range(1, n+1):
        even_num = 2 * i
        squared_num = even_num ** 2
        total_sum += squared_num
    return total_sum

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)