def last_Digit_Factorial(n): 
    if n == 0:  # Factorial of 0 is always 1
        return 1
    
    # Initialize the result to 1
    result = 1
    
    # Calculate the factorial of the number
    for i in range(1, n+1):
        result = (result * i) % 10  # Keep only the last digit
    
    return result

# Test cases




def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)