import math

def div_sum(n): 
    def sum_divisors(num): 
        s = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                s += i
                if num / i != i:
                    s += num / i
        return s

    sum1 = sum_divisors(n[0])
    sum2 = sum_divisors(n[1])

    return sum1 == sum2

# Testing the function




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)