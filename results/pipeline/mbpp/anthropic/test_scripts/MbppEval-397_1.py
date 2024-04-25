def median_numbers(a, b, c):
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers)
    median = sorted_numbers[1]
    return float(median)

def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)