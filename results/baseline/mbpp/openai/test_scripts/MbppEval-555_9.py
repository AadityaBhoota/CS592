def difference(n):
    sum_cubes = sum([i**3 for i in range(1, n+1)])
    sum_natural_numbers = sum(range(1, n+1))
    
    return sum_cubes - sum_natural_numbers

# Test cases




def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6

check(difference)