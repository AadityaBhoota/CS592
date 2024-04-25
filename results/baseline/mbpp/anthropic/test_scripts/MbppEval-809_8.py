def check_smaller(test_tup1, test_tup2):
    """
    Check if each element of the second tuple is smaller than its corresponding element in the first tuple.

    Args:
        test_tup1 (tuple): The first tuple.
        test_tup2 (tuple): The second tuple.

    Returns:
        bool: True if each element of the second tuple is smaller than its corresponding element in the first tuple, False otherwise.
    """
    if len(test_tup1) != len(test_tup2):
        return False

    for i in range(len(test_tup1)):
        if test_tup2[i] >= test_tup1[i]:
            return False

    return True

def check(candidate):
    assert check_smaller((1, 2, 3), (2, 3, 4)) == False
    assert check_smaller((4, 5, 6), (3, 4, 5)) == True
    assert check_smaller((11, 12, 13), (10, 11, 12)) == True

check(check_smaller)