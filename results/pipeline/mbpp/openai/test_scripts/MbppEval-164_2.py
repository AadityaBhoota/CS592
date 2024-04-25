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

def areEquivalent(num1, num2): 
    '''
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36, 57) == False
    areEquivalent(2, 4) == False
    areEquivalent(23, 47) == True
    '''
    def divisor_sum(n): 
        sum_divisors = 1
        for i in range(2, int(math.sqrt(n)) + 1): 
            if n % i == 0: 
                if i == (n / i): 
                    sum_divisors += i 
                else : 
                    sum_divisors += (i + n // i) 
        return sum_divisors
    
    sum_divisors_num1 = divisor_sum(num1) 
    sum_divisors_num2 = divisor_sum(num2) 
    
    return sum_divisors_num1 == sum_divisors_num2

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)