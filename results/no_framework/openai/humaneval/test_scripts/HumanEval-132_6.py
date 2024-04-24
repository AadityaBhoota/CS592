def is_nested(string):
    open_bracket_count = 0
    for char in string:
        if char == "[":
            open_bracket_count += 1
        elif char == "]" and open_bracket_count > 0:
            open_bracket_count -= 1

    return open_bracket_count < 0

# Test cases







def check(candidate):

    # Check some simple cases
    assert candidate('[[]]') == True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('[]]]]]]][[[[[]') == False
    assert candidate('[][]') == False
    assert candidate(('[]')) == False
    assert candidate('[[[[]]]]') == True
    assert candidate('[]]]]]]]]]]') == False
    assert candidate('[][][[]]') == True
    assert candidate('[[]') == False
    assert candidate('[]]') == False
    assert candidate('[[]][[') == True
    assert candidate('[[][]]') == True

    # Check some edge cases that are easy to work out by hand.
    assert candidate('') == False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate('[[[[[[[[') == False
    assert candidate(']]]]]]]]') == False


check(is_nested)