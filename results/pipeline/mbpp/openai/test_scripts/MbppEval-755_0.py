def second_smallest(numbers):
    numbers = list(set(numbers))  # Removing duplicates
    if len(numbers) < 2:
        return None
    numbers.sort()  # Sorting the list in ascending order
    return numbers[1]  # Returning the second element (index 1) as the second smallest number

def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)