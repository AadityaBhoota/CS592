def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
    return not stack

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