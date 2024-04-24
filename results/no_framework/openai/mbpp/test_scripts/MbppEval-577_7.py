def last_Digit_Factorial(n):
    # Initialize a variable to store the result
    result = 1
    
    # Calculate the factorial of the number
    for i in range(1, n+1):
        result *= i
    
    # Extract the last digit of the factorial
    last_digit = result % 10
    
    return last_digit

# Test the function with the provided examples




def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)