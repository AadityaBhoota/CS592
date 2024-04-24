def is_nested(string):
    count = 0
    for char in string:
        if char == '[':
            count += 1
        elif char == ']':
            if count > 0:
                return True
    return False

# Test cases
print(is_nested('[[]]'))           # ➞ True
print(is_nested('[]]]]]]][[[[[]'))  # ➞ False
print(is_nested('[][]'))            # ➞ False
print(is_nested('[]'))              # ➞ False
print(is_nested('[[][]]'))          # ➞ True
print(is_nested('[[]][['))          # ➞ True

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