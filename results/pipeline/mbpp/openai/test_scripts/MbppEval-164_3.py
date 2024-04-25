import math 

def div_sum(n1, n2): 
    def sum_of_divisors(num):
        div_sum = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                div_sum += i
                if i != num // i:
                    div_sum += num // i
        return div_sum
    
    sum1 = sum_of_divisors(n1)
    sum2 = sum_of_divisors(n2)
    
    return sum1 == sum2

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)