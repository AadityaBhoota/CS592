def sum(a,b):
    common_divisors = []
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)
    return sum_common_divisors(common_divisors)

def sum_common_divisors(common_divisors):
    return sum(common_divisors)

# Testing the function


def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)