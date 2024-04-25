import math 

def div_sum(n): 
    def sum_divisors(num):
        divisor_sum = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisor_sum += i
                if i != num // i:
                    divisor_sum += num // i
        return divisor_sum

    return sum_divisors(n[0]) == sum_divisors(n[1])

# Test cases




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)