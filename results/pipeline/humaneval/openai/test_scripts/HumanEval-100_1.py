def make_a_pile(n):
    stones_per_level = [n]  # Step 1: Add the initial number of stones (n) to the list
    
    stones_count = n
    for i in range(1, n):
        if stones_count % 2 == 0:
            stones_count += 1
        else:
            stones_count += 2
        stones_per_level.append(stones_count)

    return stones_per_level  # Step 3: Return the list containing the number of stones per level

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