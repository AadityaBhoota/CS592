def largest_smallest_integers(lst):
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    negative_integers = [x for x in lst if x < 0]
    positive_integers = [x for x in lst if x > 0]

    if not negative_integers:
        largest_negative = None
    else:
        largest_negative = max(negative_integers)

    if not positive_integers:
        smallest_positive = None
    else:
        smallest_positive = min(positive_integers)

    return (largest_negative, smallest_positive)

def check(candidate):

    # Check some simple cases
    assert candidate([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert candidate([2, 4, 1, 3, 5, 7, 0]) == (None, 1)
    assert candidate([1, 3, 2, 4, 5, 6, -2]) == (-2, 1)
    assert candidate([4, 5, 3, 6, 2, 7, -7]) == (-7, 2)
    assert candidate([7, 3, 8, 4, 9, 2, 5, -9]) == (-9, 2)
    assert candidate([]) == (None, None)
    assert candidate([0]) == (None, None)
    assert candidate([-1, -3, -5, -6]) == (-1, None)
    assert candidate([-1, -3, -5, -6, 0]) == (-1, None)
    assert candidate([-6, -4, -4, -3, 1]) == (-3, 1)
    assert candidate([-6, -4, -4, -3, -100, 1]) == (-3, 1)

    # Check some edge cases that are easy to work out by hand.
    assert True

check(largest_smallest_integers)