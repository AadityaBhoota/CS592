def count_divisors(n) : 
    if math.sqrt(n) == int(math.sqrt(n)): 
        return "Odd"
    else : 
        return "Even"

# Test cases




def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)