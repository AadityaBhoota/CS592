def rearrange_bigger(n):
    digits = [int(d) for d in str(n)]
    for i in range(len(digits)-2, -1, -1):
        if digits[i] < digits[i+1]:
            min_greater_index = i+1
            for j in range(i+1, len(digits)):
                if digits[j] > digits[i] and digits[j] < digits[min_greater_index]:
                    min_greater_index = j
            digits[i], digits[min_greater_index] = digits[min_greater_index], digits[i]
            result = int(''.join(map(str, digits[:i+1] + sorted(digits[i+1:])))
            return result
    return False

# Test cases




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)