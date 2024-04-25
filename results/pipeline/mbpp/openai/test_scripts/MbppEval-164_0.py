import math 
def div_sum(n): 
    '''
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36,57) == False
    areEquivalent(2,4) == False
    areEquivalent(23,47) == True
    '''
import math

def areEquivalent(x, y): 
    '''
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36,57) == False
    areEquivalent(2,4) == False
    areEquivalent(23,47) == True
    '''
    
    def divisors_sum(n):
        div_sum = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                div_sum += i
                if i != n // i:
                    div_sum += n // i
        return div_sum
    
    # Implementing step 2
    div_sum_x = divisors_sum(x)
    div_sum_y = divisors_sum(y)
    
    # Implementing step 3
    return div_sum_x == div_sum_y

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)