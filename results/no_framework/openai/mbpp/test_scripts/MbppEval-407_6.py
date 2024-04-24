def rearrange_bigger(n):
    digits = list(str(n))
    for i in range(len(digits)-1, 0, -1):
        if digits[i] > digits[i-1]:
            for j in range(len(digits)-1, i-1, -1):
                if digits[j] > digits[i-1]:
                    digits[i-1], digits[j] = digits[j], digits[i-1]
                    result = int(''.join(digits[:i] + sorted(digits[i:], reverse=True)))
                    return result if result != n else False
    return False

# Test cases




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)