def difference(n):
    sum_of_squares = sum([i**2 for i in range(1, n+1)])
    sum_of_numbers = sum(range(1, n+1))

    return sum_of_squares - sum_of_numbers

# Testing the function with the provided examples



def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6

check(difference)