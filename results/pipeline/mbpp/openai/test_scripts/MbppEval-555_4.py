def difference(n):
    sum_of_cubes = (n * (n + 1) // 2)**2
    sum_of_numbers = (n * (n + 1)) // 2
    return sum_of_cubes - sum_of_numbers

def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6

check(difference)