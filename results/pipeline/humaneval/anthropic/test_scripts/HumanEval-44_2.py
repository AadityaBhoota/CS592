def change_base(x: int, base: int):
    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x //= base
    return result or '0'



METADATA = {}


def check(candidate):
    assert candidate(8, 3) == "22"
    assert candidate(9, 3) == "100"
    assert candidate(234, 2) == "11101010"
    assert candidate(16, 2) == "10000"
    assert candidate(8, 2) == "1000"
    assert candidate(7, 2) == "111"
    for x in range(2, 8):
        assert candidate(x, x + 1) == str(x)


check(change_base)