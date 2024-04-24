import math

def div_sum(n):
    def sum_divisors(num):
        divisors = [1]
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return sum(divisors)

    sum1 = sum_divisors(n[0])
    sum2 = sum_divisors(n[1])

    return sum1 == sum2

# Test cases




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)