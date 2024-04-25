def make_a_pile(n):
    stones_in_each_level = []
    stones_in_each_level.append(n)
    
    current_level_stones = n
    for _ in range(n - 1):
        if current_level_stones % 2 == 0:
            current_level_stones += 1
        else:
            current_level_stones += 2
        stones_in_each_level.append(current_level_stones)
    
    return stones_in_each_level

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