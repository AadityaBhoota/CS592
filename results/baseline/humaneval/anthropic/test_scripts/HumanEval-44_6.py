def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    """
    # Check if the base is valid
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9 (inclusive)")

    # Initialize an empty string to store the result
    result = ""

    # Handle negative numbers
    if x < 0:
        result = "-"
        x = abs(x)

    # Convert the number to the new base
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x //= base

    # If the input is 0, return "0"
    if not result:
        result = "0"

    return result



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