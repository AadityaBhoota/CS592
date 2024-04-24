def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # Check if the input is valid (x and y are positive)
    if x < 0 or y < 0:
        return -1
    
    # Determine the largest even number in the range [x, y]
    if x % 2 == 0:
        largest_even = x
    else:
        largest_even = x + 1
    
    if largest_even <= y:
        return largest_even
    else:
        return -1

def check(candidate):

    # Check some simple cases
    assert candidate(12, 15) == 14
    assert candidate(13, 12) == -1
    assert candidate(33, 12354) == 12354
    assert candidate(5234, 5233) == -1
    assert candidate(6, 29) == 28
    assert candidate(27, 10) == -1

    # Check some edge cases that are easy to work out by hand.
    assert candidate(7, 7) == -1
    assert candidate(546, 546) == 546


check(choose_num)