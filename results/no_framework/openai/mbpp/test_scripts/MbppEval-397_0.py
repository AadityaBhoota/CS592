def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    
    return numbers[1] if (numbers[0] <= numbers[1] <= numbers[2]) or (numbers[2] <= numbers[1] <= numbers[0]) else numbers[2] if numbers[0] <= numbers[2] <= numbers[1] else numbers[0]

# Test cases




def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)