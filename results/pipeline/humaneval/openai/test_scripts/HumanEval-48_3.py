def is_palindrome(text: str):
    text = text.replace(" ", "")
    text = text.lower()
    return text == text[::-1]



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