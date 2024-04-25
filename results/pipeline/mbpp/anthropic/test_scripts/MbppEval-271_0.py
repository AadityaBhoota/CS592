def even_Power_Sum(n):
    return 2 ** 5 * (n * (n + 1) * (2 * n + 1) * (3 * n ** 2 + 3 * n - 1) / 30)

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)