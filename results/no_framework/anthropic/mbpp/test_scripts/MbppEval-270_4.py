def sum_even_and_even_index(arr, length):
    """
    Find the sum of even numbers at even positions of a list.

    Args:
        arr (list): The input list.
        length (int): The length of the list.

    Returns:
        int: The sum of even numbers at even positions.
    """
    total = 0
    for i in range(0, length, 2):
        if arr[i] % 2 == 0:
            total += arr[i]
    return total

def check(candidate):
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12

check(sum_even_and_even_index)