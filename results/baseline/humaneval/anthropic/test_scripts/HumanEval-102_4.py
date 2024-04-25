def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # Check if the input numbers are positive
    if x <= 0 or y <= 0:
        return -1
    
    # Determine the range of numbers to check
    start = max(x, y)
    end = min(x, y)
    
    # Find the biggest even integer number in the range
    for num in range(start, end-1, -2):
        if num >= end:
            return num
    
    # If no even integer number is found, return -1
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