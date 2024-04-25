def largest_neg(list1):
    """
    Write a python function to find the largest negative number from the given list.

    Examples:
    largest_neg([1,2,3,-4,-6]) == -6
    largest_neg([1,2,3,-8,-9]) == -9
    largest_neg([1,2,3,4,-1]) == -1
    """
    negatives = [num for num in list1 if num < 0]
    if not negatives:
        return None
    return max(negatives)

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)