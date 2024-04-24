def overlapping(list1, list2):
    """
    Checks whether any value in one sequence exists in the other sequence.

    Args:
        list1 (list): The first sequence.
        list2 (list): The second sequence.

    Returns:
        bool: True if any value in the sequences overlaps, False otherwise.
    """
    return bool(set(list1) & set(list2))

def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True

check(overlapping)