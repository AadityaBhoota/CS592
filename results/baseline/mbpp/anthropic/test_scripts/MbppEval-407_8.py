def rearrange_bigger(n):
    """
    Write a function to create the next bigger number by rearranging the digits of a given number.

    Examples:
    rearrange_bigger(12) == 21
    rearrange_bigger(10) == False
    rearrange_bigger(102) == 120
    """
    # Convert the number to a list of digits
    digits = [int(d) for d in str(n)]

    # Find the first digit from the right that is smaller than the next digit
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    # If i is -1, the number is already the largest possible, so return False
    if i == -1:
        return False

    # Find the smallest digit to the right of i that is greater than digits[i]
    j = len(digits) - 1
    while j > i and digits[j] <= digits[i]:
        j -= 1

    # Swap the digits at i and j
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the digits to the right of i
    digits[i+1:] = digits[i+1:][::-1]

    # Convert the list of digits back to a number and return it
    return int(''.join(map(str, digits)))

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)