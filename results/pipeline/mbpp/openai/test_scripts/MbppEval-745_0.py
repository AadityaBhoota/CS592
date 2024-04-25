def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        is_divisible = all(int(digit_char) != 0 and num % int(digit_char) == 0 for digit_char in str(num))
        if is_divisible:
            result.append(num)
    return result

def check(candidate):
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert divisible_by_digits(20,25)==[22, 24]

check(divisible_by_digits)