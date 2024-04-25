def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()

    if len(numbers) % 2 == 0:
        mid_left = len(numbers) // 2 - 1
        mid_right = len(numbers) // 2
        median = (numbers[mid_left] + numbers[mid_right]) / 2
    else:
        median = numbers[len(numbers) // 2]

    return median





def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)