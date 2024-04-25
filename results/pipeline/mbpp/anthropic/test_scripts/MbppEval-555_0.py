def difference(n):
    sum_cubes = sum(i**3 for i in range(1, n+1))
    sum_numbers = sum(range(1, n+1))
    return sum_cubes - sum_numbers

def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6

check(difference)