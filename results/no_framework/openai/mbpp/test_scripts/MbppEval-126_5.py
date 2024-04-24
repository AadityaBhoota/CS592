def find_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def sum_of_common_divisors(a, b):
    divisors_a = find_divisors(a)
    divisors_b = find_divisors(b)
    
    common_divisors = set(divisors_a) & set(divisors_b)
    
    return sum(common_divisors)

# Testing the function with the given examples




def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)