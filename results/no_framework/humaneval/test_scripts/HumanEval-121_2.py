def solution(lst):
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 != 0)

# Test cases
print(solution([5, 8, 7, 1]))  # Output should be 12
print(solution([3, 3, 3, 3, 3]))  # Output should be 9
print(solution([30, 13, 24, 321]))  # Output should be 0

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