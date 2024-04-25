def rearrange_bigger(n):
    """
    Write a function to create the next bigger number by rearranging the digits of a given number.

    Examples:
    rearrange_bigger(12) == 21
    rearrange_bigger(10) == False
    rearrange_bigger(102) == 120
    """
    n_str = str(n)
    n_digits = list(n_str)
    
    # Find the rightmost digit that is smaller than the digit to its right
    i = len(n_digits) - 2
    while i >= 0 and n_digits[i] >= n_digits[i+1]:
        i -= 1
    
    if i < 0:
        return False
    
    # Find the smallest digit to the right of i that is larger than n_digits[i]
    j = len(n_digits) - 1
    while j > i and n_digits[j] <= n_digits[i]:
        j -= 1
    
    # Swap the digits at i and j
    n_digits[i], n_digits[j] = n_digits[j], n_digits[i]
    
    # Reverse the digits to the right of i
    n_digits[i+1:] = n_digits[i+1:][::-1]
    
    return int(''.join(n_digits))

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)