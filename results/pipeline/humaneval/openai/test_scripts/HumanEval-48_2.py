def is_palindrome(text: str):
    pointer1 = 0
    pointer2 = len(text) - 1

    while pointer1 < pointer2:
        if text[pointer1] != text[pointer2]:
            return False
        
        pointer1 += 1
        pointer2 -= 1
    
    return True



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