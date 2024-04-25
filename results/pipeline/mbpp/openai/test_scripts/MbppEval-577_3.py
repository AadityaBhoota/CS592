def last_Digit_Factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    last_digit = result % 10
    return last_digit

def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)