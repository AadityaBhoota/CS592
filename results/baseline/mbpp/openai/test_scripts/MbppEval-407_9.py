def rearrange_bigger(n):
    n = str(n)
    digits = [int(d) for d in n]

    i = len(digits) - 1
    while i > 0 and digits[i - 1] >= digits[i]:
        i -= 1

    if i == 0:
        return False

    j = len(digits) - 1
    while digits[j] <= digits[i - 1]:
        j -= 1

    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = sorted(digits[i:])

    result = int(''.join(map(str, digits)))
    return result

# Test cases




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)