def median_numbers(a, b, c):
    numbers_list = [a, b, c]
    sorted_numbers = sorted(numbers_list)
    
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2] + sorted_numbers[n//2 - 1]) / 2
    else:
        median = sorted_numbers[n//2]
    
    return median

def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)