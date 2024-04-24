def is_palindrome(text: str) -> bool:
    return text == text[::-1]

# Test cases
print(is_palindrome(''))      # True
print(is_palindrome('aba'))   # True
print(is_palindrome('aaaaa')) # True
print(is_palindrome('zbcd'))  # False



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