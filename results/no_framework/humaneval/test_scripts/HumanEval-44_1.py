def change_base(x: int, base: int):
    if x < 0 or base < 2 or base > 9:
        return "Invalid input"

    if x == 0:
        return '0'

    result = ""
    while x > 0:
        digit = x % base
        result = str(digit) + result
        x //= base

    return result

print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'



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