def second_smallest(numbers):
    """
    Write a function to find the second smallest number in a list.

    Examples:
    second_smallest([1, 2, -8, -2, 0, -2]) == -2
    second_smallest([1, 1, -0.5, 0, 2, -2, -2]) == -0.5
    second_smallest([2,2]) == None
    """
    if len(numbers) < 2:
        return None

    # Sort the list in ascending order
    numbers.sort()

    # Find the second smallest number
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[0]:
            return numbers[i]

    # If all numbers in the list are the same, return None
    return None

def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)