def vowels_count(s):
    count = 0
    end_vowel = False
    vowels = 'aeiouy'

    for char in s.lower():
        if char in vowels:
            count += 1
            if char == 'y':
                end_vowel = True
        else:
            end_vowel = False

    # Check if last character is 'y' and consider it as a vowel
    if end_vowel:
        count -= 1

    return count

# Test cases






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