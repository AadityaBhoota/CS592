def sum(a, b):
    def common_divisors(a, b):
        divisors_a = [i for i in range(1, a+1) if a % i == 0]
        divisors_b = [i for i in range(1, b+1) if b % i == 0]
        
        common_divisors = set(divisors_a) & set(divisors_b)
        
        return list(common_divisors)
    
    common_div = common_divisors(a, b)
    return sum(common_div)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)