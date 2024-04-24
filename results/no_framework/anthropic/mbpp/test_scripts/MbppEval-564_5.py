def count_Pairs(arr, n):
    """
    Counts the number of possible unordered pairs where both elements are unequal.

    Args:
        arr (list): A list of integers.
        n (int): The length of the list.

    Returns:
        int: The count of unordered pairs where both elements are unequal.
    """
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] != arr[j]:
                count += 1
    return count

def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)