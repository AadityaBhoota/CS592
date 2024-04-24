def sum_even_and_even_index(arr, n):
    """
    Find the sum of even numbers at even positions of a list until the nth element.

    Parameters:
    arr (list): The input list of integers.
    n (int): The position until which the sum should be calculated.

    Returns:
    int: The sum of even numbers at even positions.

    Examples:
    sum_even_and_even_index([5, 6, 12, 1, 18, 8], 6) == 30
    sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18], 10) == 26
    sum_even_and_even_index([5, 6, 12, 1], 4) == 12
    """
    total_sum = 0
    for i in range(n):
        if i % 2 == 0 and arr[i] % 2 == 0:  # Check if index is even and value is even
            total_sum += arr[i]
    return total_sum

# Test cases




def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12

check(sum_even_and_even_index)