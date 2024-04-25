def rearrange_bigger(n):
    """
    Write a function to create the next bigger number by rearranging the digits of a given number.
    
    Examples:
    rearrange_bigger(12) == 21
    rearrange_bigger(10) == False
    rearrange_bigger(102) == 120
    """
    digits = list(str(n))
    
    # Find the first digit from the right that is smaller than the digit to its right
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1
    
    if i < 0:
        return False
    
    # Find the smallest digit to the right of the digit found in the previous step
    # that is greater than it
    j = len(digits) - 1
    while j > i and digits[j] <= digits[i]:
        j -= 1
    
    # Swap the two digits
    digits[i], digits[j] = digits[j], digits[i]
    
    # Reverse the digits to the right of the swapped digits
    digits[i+1:] = digits[i+1:][::-1]
    
    return int(''.join(digits))

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)