def sum(a,b): 
    '''
    Write a python function to find the sum of common divisors of two given numbers.

    Examples:
    sum(10,15) == 6
    sum(100,150) == 93
    sum(4,6) == 3
    '''
def common_divisors(a, b):
    def find_divisors(num):
        divisors = set()
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        return divisors

    divisors_a = find_divisors(a)
    divisors_b = find_divisors(b)
    
    common_divisors = divisors_a.intersection(divisors_b)
    
    return sum(common_divisors)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)