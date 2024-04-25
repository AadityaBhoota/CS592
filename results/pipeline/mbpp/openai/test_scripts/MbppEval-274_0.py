import math  
def even_binomial_Coeff_Sum(n): 
    if not isinstance(n, int) or n <= 0:
        return "Please enter a positive integer for n"
    
    # Step 1: Calculate the sum of even index binomial coefficients
    sum_even_binomial = 2**n
    
    return sum_even_binomial

def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)