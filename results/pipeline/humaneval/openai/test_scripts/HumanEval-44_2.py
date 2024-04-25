def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Step 0: Validate base
    if base >= 10:
        return "Base should be less than 10."

    # Step 1: Initialize an empty string to store the converted result
    result = ""
    
    # Step 2: Convert the number to the new base
    while x > 0:
        remainder = x % base
        result = str(remainder) + result  # Build the converted number in reverse order
        x //= base

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