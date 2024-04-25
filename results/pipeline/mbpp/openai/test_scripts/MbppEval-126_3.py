def sum_of_common_divisors(a, b):
    common_divisors = []
    
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)
    
    return sum(common_divisors)

# Test the function with examples




def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)