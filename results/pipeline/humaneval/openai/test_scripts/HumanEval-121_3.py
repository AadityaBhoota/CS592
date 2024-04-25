def solution(lst):
    odd_elements_sum = 0
    for index, num in enumerate(lst):
        if num % 2 != 0 and index % 2 == 0:  # Check if the element is odd and the index is even
            odd_elements_sum += num  # Add the odd element to the sum

    return odd_elements_sum

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