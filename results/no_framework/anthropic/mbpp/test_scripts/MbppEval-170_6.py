def sum_range_list(list1, m, n):
    """
    Write a function to find the sum of numbers in a list within a range specified by two indices.

    Examples:
    sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10) == 29
    sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 5, 7) == 16
    sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 7, 10) == 38
    """
    if m < 0 or n >= len(list1):
        return -1  # Return -1 if the indices are out of range

    total = 0
    for i in range(m, n + 1):
        total += list1[i]

    return total

def check(candidate):
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38

check(sum_range_list)