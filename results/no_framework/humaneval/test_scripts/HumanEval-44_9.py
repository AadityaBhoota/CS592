def change_base(x: int, base: int) -> str:
    if x < 0:
        return "-" + change_base(-x, base)
    alphabet = "0123456789"
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        x, remainder = divmod(x, base)
        result = alphabet[remainder] + result
    return result

# Testing the function
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'



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