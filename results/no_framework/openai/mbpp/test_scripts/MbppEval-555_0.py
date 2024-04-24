def difference(n):
    sum_of_squares = n*(n+1)//2
    square_of_sum = (n*(n+1)//2)**2
    return square_of_sum - sum_of_squares

# Test cases




def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6

check(difference)