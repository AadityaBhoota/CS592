def is_palindrome(text: str) -> bool:
    return text == text[::-1]

# Testing the function with given test cases
print(is_palindrome(''))     # Output: True
print(is_palindrome('aba'))  # Output: True
print(is_palindrome('aaaaa'))  # Output: True
print(is_palindrome('zbcd'))  # Output: False



METADATA = {}


def check(candidate):
    assert candidate('') == True
    assert candidate('aba') == True
    assert candidate('aaaaa') == True
    assert candidate('zbcd') == False
    assert candidate('xywyx') == True
    assert candidate('xywyz') == False
    assert candidate('xywzx') == False


check(is_palindrome)