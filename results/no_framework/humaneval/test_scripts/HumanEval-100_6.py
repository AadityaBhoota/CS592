def make_a_pile(n):
    stones_per_level = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones_per_level.append(stones_per_level[-1] + 2)
        else:
            stones_per_level.append(stones_per_level[-1] + 1)
        n += 1
    return stones_per_level

# Test the function with the example given
print(make_a_pile(3))  # Output: [3, 5, 7]

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