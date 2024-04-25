def rearrange_bigger(n):
    digits = [int(d) for d in str(n)]
    
    for i in range(len(digits) - 1, 0, -1):
        if digits[i - 1] < digits[i]:
            break

    if i == 1 and digits[i] <= digits[i - 1]:
        return False

    pivot = i - 1

    for j in range(len(digits) - 1, pivot, -1):
        if digits[j] > digits[pivot]:
            break
            
    digits[pivot], digits[j] = digits[j], digits[pivot]
    
    digits[pivot+1:] = sorted(digits[pivot+1:])
    
    return int(''.join(map(str, digits)))

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)