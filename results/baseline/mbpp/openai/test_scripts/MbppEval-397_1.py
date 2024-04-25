def median_numbers(a, b, c):
    # Create a list of the three numbers
    numbers = [a, b, c]
    # Sort the list
    numbers.sort()
    
    # Check if the length of the list is even or odd
    if len(numbers) % 2 == 0:
        # If the length of the list is even, return the average of the middle two numbers
        return (numbers[1] + numbers[2]) / 2
    else:
        # If the length of the list is odd, return the middle number
        return numbers[1]

# Test cases




def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)