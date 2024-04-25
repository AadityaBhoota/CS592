def make_a_pile(n):
    stone_pile = [n]  # Append n to the list, representing the first level

    for i in range(2, n+1):  # Loop from level 2 to n (inclusive)
        if stone_pile[i-2] % 2 == 0:  # Check if the stones in the previous level are even
            stone_pile.append(stone_pile[i-2] + 1)  # If even, add the next odd number of stones
        else:
            stone_pile.append(stone_pile[i-2] + 2)  # If odd, add the next even number of stones

    return stone_pile

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