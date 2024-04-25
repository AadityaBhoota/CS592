def vowels_count(s):
    vowels = 'aeiouy'
    count = 0
    s = s.lower()  # Convert input string to lower case to handle both upper and lower case vowels

    if s and s[-1] == 'y':  # If the last character is 'y', consider it as a vowel
        count += 1

    for char in s:
        if char in vowels:
            count += 1

    return count

# Test cases
def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("python") == 1
    assert vowels_count("Hello") == 2
    assert vowels_count("") == 0
    assert vowels_count("sky") == 1

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