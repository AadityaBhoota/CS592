def median_numbers(a, b, c):
    sorted_numbers = sorted([a, b, c])
    return sorted_numbers[1]

# Test the function with examples




def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)