def rearrange_bigger(n):
    digits = [int(d) for d in str(n)]
    
    # Find the pivot point where the number decreases
    pivot = -1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            pivot = i - 1
            break
    
    # If no pivot point is found, return False
    if pivot == -1:
        return False
    
    # Find the smallest digit after the pivot point that is greater than the digit at the pivot
    for i in range(len(digits) - 1, pivot, -1):
        if digits[i] > digits[pivot]:
            digits[i], digits[pivot] = digits[pivot], digits[i]
            break
    
    # Reverse the digits after the pivot point to get the next bigger number
    digits[pivot + 1:] = reversed(digits[pivot + 1:])
    
    # Convert the list of digits back to a number
    result = int(''.join(map(str, digits)))
    
    return result

# Test cases




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)