def largest_smallest_integers(lst):
    neg_integers = [num for num in lst if num < 0]
    pos_integers = [num for num in lst if num > 0]

    max_neg = max(neg_integers) if neg_integers else None
    min_pos = min(pos_integers) if pos_integers else None

    return (max_neg, min_pos)

# Test cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)

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