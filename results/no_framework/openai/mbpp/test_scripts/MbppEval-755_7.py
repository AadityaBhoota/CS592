def second_smallest(numbers):
    unique_numbers = list(set(numbers))  # Get unique numbers in the list
    unique_numbers.sort()  # Sort the unique numbers
    if len(unique_numbers) < 2:  # If there are less than 2 unique numbers
        return None
    return unique_numbers[1]  # Return the second smallest number

# Test cases




def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)