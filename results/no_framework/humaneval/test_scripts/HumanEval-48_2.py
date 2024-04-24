def  is_palindrome(text: str) -> bool:
    return text == text[::-1]

# Testing the function with the given test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()



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