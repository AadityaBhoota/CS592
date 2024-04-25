import math

def div_sum(n1, n2):
    def sum_of_divisors(n):
        result = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                result += i
                if i != n // i:
                    result += n // i
        return result
    
    return sum_of_divisors(n1) == sum_of_divisors(n2)

# Test cases




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)