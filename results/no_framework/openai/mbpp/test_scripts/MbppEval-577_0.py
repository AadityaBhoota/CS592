def last_digit_factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result = (result * i) % 10
        return result

# Test cases




def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)