def even_Power_Sum(n):
    sum_result = 0
    count = 0
    num = 2

    while count < n:
        if num % 2 == 0:
            sum_result += num ** 5
            count += 1
        num += 2

    return sum_result

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)