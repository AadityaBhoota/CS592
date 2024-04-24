def last_digit_factorial(n):
    if n == 0:
        return 1

    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        factorial %= 10  # Keep only the last digit to avoid overflow

    return factorial

# Test cases




def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)