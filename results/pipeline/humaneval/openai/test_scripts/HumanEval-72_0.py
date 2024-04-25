def will_it_fly(q, w):
    def is_palindrome(lst):
        return lst == lst[::-1]

    def sum_elements(lst):
        return sum(lst)

    if is_palindrome(q) and sum_elements(q) <= w:
        return True
    else:
        return False

def check(candidate):

    # Check some simple cases
    assert candidate([3, 2, 3], 9) is True
    assert candidate([1, 2], 5) is False
    assert candidate([3], 5) is True
    assert candidate([3, 2, 3], 1) is False


    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 3], 6) is False
    assert candidate([5], 5) is True


check(will_it_fly)