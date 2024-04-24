import math

def div_sum(n): 
    def sum_divisors(x): 
        div_sum = 1
        for i in range(2, int(math.sqrt(x)) + 1): 
            if x % i == 0: 
                div_sum += i 
                if i != x // i: 
                    div_sum += x // i 
        return div_sum

    num1, num2 = n
    return sum_divisors(num1) == sum_divisors(num2)

# Test cases




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)