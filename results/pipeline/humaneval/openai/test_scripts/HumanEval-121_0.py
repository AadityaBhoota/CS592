def solution(lst):
    sum_of_odd_at_even_positions = 0
    
    if not lst:
        return 0
    
    for index, num in enumerate(lst):
        if index % 2 == 0 and num % 2 != 0:
            sum_of_odd_at_even_positions += num
    
    return sum_of_odd_at_even_positions

def check(candidate):

    # Check some simple cases
    assert candidate([5, 8, 7, 1])    == 12
    assert candidate([3, 3, 3, 3, 3]) == 9
    assert candidate([30, 13, 24, 321]) == 0
    assert candidate([5, 9]) == 5
    assert candidate([2, 4, 8]) == 0
    assert candidate([30, 13, 23, 32]) == 23
    assert candidate([3, 13, 2, 9]) == 3

    # Check some edge cases that are easy to work out by hand.


check(solution)