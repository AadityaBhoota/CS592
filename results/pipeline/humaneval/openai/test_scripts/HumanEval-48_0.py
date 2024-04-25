def is_palindrome(text: str):
    if len(text) <= 1:
        return True
    
    if text == text[::-1]:
        return True
    else:
        return False



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