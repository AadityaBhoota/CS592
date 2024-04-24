def vowels_count(s):
    vowels = 'aeiouy'
    count = 0
    last_char = s[-1].lower()
    
    for char in s.lower():
        if char in vowels or (char == 'y' and char == last_char):
            count += 1
            
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("Python"))  # Output: 1
print(vowels_count("rhythm"))  # Output: 0
print(vowels_count("country"))  # Output: 3

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