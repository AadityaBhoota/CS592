def vowels_count(s):
    s = s.lower()
    vowels = 'aeiouy'
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            if s[i] == 'y' and i == len(s) - 1:
                count += 1
            elif s[i] != 'y':
                count += 1
    return count

# Test cases
assert vowels_count("abcde") == 2
assert vowels_count("ACEDY") == 3
assert vowels_count("Hello") == 2
assert vowels_count("Python") == 1
assert vowels_count("AEIOUY") == 6

print("All test cases pass")

def check(candidate):

    # Check some simple cases
    assert candidate("abcde") == 2, "Test 1"
    assert candidate("Alone") == 3, "Test 2"
    assert candidate("key") == 2, "Test 3"
    assert candidate("bye") == 1, "Test 4"
    assert candidate("keY") == 2, "Test 5"
    assert candidate("bYe") == 1, "Test 6"
    assert candidate("ACEDY") == 3, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(vowels_count)