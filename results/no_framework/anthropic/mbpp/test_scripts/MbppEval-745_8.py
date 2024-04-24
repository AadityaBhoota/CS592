def divisible_by_digits(startnum, endnum):
    """
    Write a function to find numbers within a given range from startnum to endnum where every number is divisible by every digit it contains.
    """
    result = []
    for num in range(startnum, endnum + 1):
        digits = set(str(num))
        if all(num % int(d) == 0 for d in digits):
            result.append(num)
    return result

def check(candidate):
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert divisible_by_digits(20,25)==[22, 24]

check(divisible_by_digits)