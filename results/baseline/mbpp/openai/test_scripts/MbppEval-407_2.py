def rearrange_bigger(n):
    digits = [int(d) for d in str(n)]
    
    for i in range(len(digits)-1, 0, -1):
        if digits[i] > digits[i-1]:
            # Find the smallest digit after i-1 that is greater than digits[i-1]
            swap_index = i
            for j in range(i, len(digits)):
                if digits[j] > digits[i-1] and digits[j] <= digits[swap_index]:
                    swap_index = j
            
            # Swap the two digits 
            digits[i-1], digits[swap_index] = digits[swap_index], digits[i-1]
            
            # Sort the digits after i-1 in ascending order
            digits[i:] = sorted(digits[i:])
            
            return int(''.join(map(str, digits)))
    
    return False

# Test cases




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)