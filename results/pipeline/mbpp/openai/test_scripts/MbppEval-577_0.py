def last_Digit_Factorial(n): 
    '''
    Write a python function to find the last digit in the factorial of a given number.
    
    Examples:
    last_Digit_Factorial(4) == 4
    last_Digit_Factorial(21) == 0
    last_Digit_Factorial(30) == 0
    '''
    fact = 1
    
    for i in range(1, n+1):
        fact *= i
    
    last_digit = fact % 10
    
    return last_digit

def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)