def will_it_fly(q, w):
    # Check if the list q is balanced (palindromic)
    if q != q[::-1]:
        return False
    
    # Check if the sum of elements in q is less than or equal to the maximum possible weight w
    if sum(q) <= w:
        return True
    else:
        return False

# Test cases
print(will_it_fly([1, 2], 5))  # ➞ False
print(will_it_fly([3, 2, 3], 1))  # ➞ False
print(will_it_fly([3, 2, 3], 9))  # ➞ True
print(will_it_fly([3], 5))  # ➞ True

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