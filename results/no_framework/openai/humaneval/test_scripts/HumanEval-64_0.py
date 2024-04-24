def vowels_count(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitive matching
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    
    count = 0
    last_char_is_y = False
    
    for i, char in enumerate(s):
        if char in vowels:
            if char == 'y' and i == len(s) - 1:
                last_char_is_y = True
            else:
                count += 1

    return count + int(last_char_is_y)

# Test cases
def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("sky") == 1
    assert vowels_count("aeiouy") == 6
    assert vowels_count("zzzzz") == 0
    assert vowels_count("") == 0
    assert vowels_count("Python") == 1

    print("All test cases pass")

if __name__ == "__main__":
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