def rearrange_bigger(n):
    digits = [int(d) for d in str(n)]
    for i in range(len(digits)-1, 0, -1):
        if digits[i-1] < digits[i]:
            smaller_digit_index = i - 1
            break
    else:
        return False
    for j in range(len(digits)-1, smaller_digit_index, -1):
        if digits[j] > digits[smaller_digit_index]:
            bigger_digit_index = j
            break
    digits[smaller_digit_index], digits[bigger_digit_index] = digits[bigger_digit_index], digits[smaller_digit_index]
    digits[smaller_digit_index+1:] = sorted(digits[smaller_digit_index+1:])
    result = int(''.join(map(str, digits)))
    return result

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)