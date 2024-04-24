def vowels_count(s):
    s = s.lower()
    vowels = 'aeiouy'
    count = 0
    last_char = s[-1]
    
    for char in s:
        if char in vowels:
            if char == 'y' and char != last_char:
                continue
            count += 1
    
    return count

# Test cases
def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("Python") == 1
    assert vowels_count("Hello") == 2
    assert vowels_count("qwrtyp") == 0
    assert vowels_count("Python is amazing") == 6
    assert vowels_count("") == 0

test_vowels_count()

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