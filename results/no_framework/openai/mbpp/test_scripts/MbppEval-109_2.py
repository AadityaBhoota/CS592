def odd_Equivalent(s, n):
    def count_odd(s):
        return sum(1 for digit in s if digit == '1')

    original_odd_count = count_odd(s)
    cycle_len = len(s)

    odd_count = original_odd_count * (n // cycle_len) + count_odd(s[:n % cycle_len])

    return odd_count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)