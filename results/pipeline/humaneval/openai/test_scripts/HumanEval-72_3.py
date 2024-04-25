def is_palindromic(lst):
    return lst == lst[::-1]

def will_it_fly(q, w):
    if not is_palindromic(q):
        return False
    
    sum_elements = sum(q)
    
    if sum_elements <= w:
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