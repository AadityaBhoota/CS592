def even_Power_Sum(n):
    return (2 * n * (2 * n + 1) * (2 * n + 2) * (2 * n + 3) * (2 * n + 4)) // 5
def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)