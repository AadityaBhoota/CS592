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

    # Find the first digit from the right that is smaller than the digit to its right
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    # If i is -1, it means the number is already the largest possible number, so return False
    if i == -1:
        return False

    # Find the first digit from the right that is larger than digits[i]
    j = len(digits) - 1
    while j > i and digits[j] <= digits[i]:
        j -= 1

    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the digits to the right of digits[i]
    digits[i + 1:] = digits[i + 1:][::-1]

    # Convert the list of digits back to a number and return it
    return int(''.join(digits))

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)