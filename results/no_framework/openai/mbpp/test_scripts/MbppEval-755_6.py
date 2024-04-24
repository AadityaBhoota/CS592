def second_smallest(numbers):
    unique_numbers = set(numbers)  # Get unique numbers to exclude duplicates

    if len(unique_numbers) < 2:
        return None  # If there are fewer than 2 unique numbers, return None

    sorted_numbers = sorted(unique_numbers)  # Sort the unique numbers
    return sorted_numbers[1]  # Return the second smallest number

# Test cases




def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)