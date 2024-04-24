def histogram(test):
    if not test:
        return {}

    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Iterate through the string and count the occurrences of each letter
    for letter in test.split():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Find the maximum count of any letter
    max_count = max(letter_count.values())

    # Create a new dictionary with the letters that have the maximum count
    result = {k: v for k, v in letter_count.items() if v == max_count}

    return result

def check(candidate):

    # Check some simple cases
    assert candidate('a b b a') == {'a':2,'b': 2}, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('a b c a b') == {'a': 2, 'b': 2}, "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, "This prints if this assert fails 3 (good for debugging!)"
    assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}, "This prints if this assert fails 4 (good for debugging!)"
    assert candidate('b b b b a') == {'b': 4}, "This prints if this assert fails 5 (good for debugging!)"
    assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}, "This prints if this assert fails 6 (good for debugging!)"
    
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('') == {}, "This prints if this assert fails 7 (also good for debugging!)"
    assert candidate('a') == {'a': 1}, "This prints if this assert fails 8 (also good for debugging!)"


check(histogram)