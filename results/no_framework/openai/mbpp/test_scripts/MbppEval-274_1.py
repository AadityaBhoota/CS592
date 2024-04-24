def even_binomial_coeff_sum(n):
    # Initialize the result variable to store the sum of even index binomial coefficients
    result = 0
    
    # Calculate the binomial coefficients using the formula nCr = n! / (r! * (n-r)!)
    for r in range(n//2 + 1):
        coeff = math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
        
        # If the index is even, add the coefficient to the result
        if r % 2 == 0:
            result += coeff
            
    return result

# Test cases




def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)