def rearrange_bigger(n):
    if n < 10:
        return False
    
    digits = [int(d) for d in str(n)]

    for i in range(len(digits)-2, -1, -1):
        if digits[i] < digits[i+1]:
            break
    else:
        return False

    for j in range(len(digits)-1, i, -1):
        if digits[j] > digits[i]:
            break

    digits[i], digits[j] = digits[j], digits[i]
    digits[i+1:] = sorted(digits[i+1:])

    return int(''.join(map(str, digits)))





def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)