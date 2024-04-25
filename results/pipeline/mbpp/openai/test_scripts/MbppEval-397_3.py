def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    
    if len(numbers) % 2 == 1:
        return numbers[len(numbers)//2]
    else:
        mid = len(numbers)//2
        return (numbers[mid-1] + numbers[mid]) / 2

def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)