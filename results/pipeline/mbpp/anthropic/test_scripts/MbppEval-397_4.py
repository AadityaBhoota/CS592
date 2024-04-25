def median_numbers(a, b, c):
    min_num = min(a, b, c)
    max_num = max(a, b, c)
    middle_value = (a + b + c) - min_num - max_num
    median = middle_value / 2
    return median

def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)