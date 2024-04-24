def last_Digit_Factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        last_digit = 1
        for i in range(2, n + 1):
            last_digit = (last_digit * i) % 10
        return last_digit

# Test the function with the provided examples




def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)