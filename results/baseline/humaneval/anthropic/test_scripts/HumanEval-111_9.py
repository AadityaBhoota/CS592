def histogram(test):
    if not test:
        return {}

    char_count = {}
    for char in test.split():
        char_count[char] = char_count.get(char, 0) + 1

    max_count = max(char_count.values())
    return {char: count for char, count in char_count.items() if count == max_count}

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