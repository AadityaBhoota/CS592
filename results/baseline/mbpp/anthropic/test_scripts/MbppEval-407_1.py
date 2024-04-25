def rearrange_bigger(n):
    """
    Write a function to create the next bigger number by rearranging the digits of a given number.

    Examples:
    rearrange_bigger(12) == 21
    rearrange_bigger(10) == False
    rearrange_bigger(102) == 120
    """
    # Convert the number to a list of digits
    digits = list(str(n))

    # Find the rightmost digit that is smaller than the digit to its right
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1

    # If we reach the beginning of the list, the number cannot be rearranged
    if i < 0:
        return False

    # Find the smallest digit to the right of i that is larger than digits[i]
    j = len(digits) - 1
    while j > i and digits[j] <= digits[i]:
        j -= 1

    # Swap the digits at positions i and j
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the digits to the right of i
    digits[i+1:] = digits[i+1:][::-1]

    # Convert the list of digits back to an integer and return it
    return int(''.join(digits))

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)