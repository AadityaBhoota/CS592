def will_it_fly(q, w):
    def is_palindromic_list(lst):
        return lst == lst[::-1]
    
    is_balanced = is_palindromic_list(q)
    sum_of_elements = sum(q)
    is_under_weight = sum_of_elements <= w
    
    return is_balanced and is_under_weight

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