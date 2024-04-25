def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(number):
        digits = [int(digit) for digit in str(number) if int(digit) != 0]
        return all(number % digit == 0 for digit in digits)

    results = []
    for num in range(startnum, endnum + 1):
        if is_divisible_by_digits(num):
            results.append(num)
    
    return results

# Test cases




def check(candidate):
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert divisible_by_digits(20,25)==[22, 24]

check(divisible_by_digits)