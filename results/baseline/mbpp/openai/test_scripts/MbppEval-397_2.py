def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    
    if len(numbers) % 2 == 0:
        mid = len(numbers) // 2
        median = (numbers[mid - 1] + numbers[mid]) / 2
    else:
        mid = len(numbers) // 2
        median = numbers[mid]
    
    return median

# Test the function




def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)