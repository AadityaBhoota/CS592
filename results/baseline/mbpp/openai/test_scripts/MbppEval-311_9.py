def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    binary_str = bin(n)[2:]
    for i in range(len(binary_str)):
        if binary_str[i] == '0':
            return n + 2**(len(binary_str) - i - 1)
    return n

# Test cases




def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)