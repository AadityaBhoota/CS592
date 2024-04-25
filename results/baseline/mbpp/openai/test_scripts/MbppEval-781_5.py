def count_divisors(n):
    if math.sqrt(n).is_integer():
        return "Odd"
    else:
        return "Even"

# Test cases
assert count_divisors(10) == "Even"
assert count_divisors(100) == "Odd"
assert count_divisors(125) == "Even"

def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)