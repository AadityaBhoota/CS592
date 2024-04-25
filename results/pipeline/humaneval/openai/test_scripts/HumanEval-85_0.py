def add(lst):
    sum_of_even_at_odd_indices = 0
    
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            sum_of_even_at_odd_indices += lst[i]
    
    return sum_of_even_at_odd_indices

def check(candidate):

    # Check some simple cases
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    

check(add)