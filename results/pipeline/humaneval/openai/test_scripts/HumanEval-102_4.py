def choose_num(x, y):
    if x <= 0 or y <= 0:
        return -1

    # Step 1: Check if both x and y are positive and even numbers
    if x % 2 != 0:
        x += 1  # Make x even if it's not already
    if y % 2 != 0:
        y -= 1  # Make y even if it's not already

    # Step 2: Find the biggest even number in the range [x, y]
    for i in range(y, x - 1, -2):
        if i % 2 == 0:
            return i

    return -1  # No even number in the range

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