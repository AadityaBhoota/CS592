def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).
    
    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    stones_per_level = [n]  # Store the stones in the first level
    current_stones = n
    
    for i in range(n - 1):  # Iterate n times for n levels of stones
        if current_stones % 2 == 0:
            current_stones += 1  # Next odd number of stones for even current stones
        else:
            current_stones += 2  # Next even number of stones for odd current stones
        stones_per_level.append(current_stones)  # Store the stones in the next level

    return stones_per_level

def check(candidate):

    # Check some simple cases
    assert candidate(3) == [3, 5, 7], "Test 3"
    assert candidate(4) == [4,6,8,10], "Test 4"
    assert candidate(5) == [5, 7, 9, 11, 13]
    assert candidate(6) == [6, 8, 10, 12, 14, 16]
    assert candidate(8) == [8, 10, 12, 14, 16, 18, 20, 22]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(make_a_pile)