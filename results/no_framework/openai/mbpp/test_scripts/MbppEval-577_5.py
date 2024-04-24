def last_Digit_Factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n+1):
        result = (result * i) % 10

    return result

def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)