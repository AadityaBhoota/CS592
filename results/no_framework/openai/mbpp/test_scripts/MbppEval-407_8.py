def rearrange_bigger(n):
    # Convert the number to a list of digits
    digits = [int(d) for d in str(n)]
    
    # Find the index of the first digit that is smaller than the next digit in reverse order
    pivot = -1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            pivot = i - 1
            break
    
    # If no such digit is found, return False
    if pivot == -1:
        return False
    
    # Find the smallest digit to the right of the pivot that is just greater than pivot
    next_larger = pivot + 1
    for i in range(pivot + 1, len(digits)):
        if digits[i] > digits[pivot] and digits[i] < digits[next_larger]:
            next_larger = i
    
    # Swap the pivot and next larger digit
    digits[pivot], digits[next_larger] = digits[next_larger], digits[pivot]
    
    # Sort the digits to the right of the pivot
    digits[pivot + 1:] = sorted(digits[pivot + 1:])
    
    # Convert the list of digits back to a number
    result = int(''.join(map(str, digits)))
    
    return result

# Test the function with some examples




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)