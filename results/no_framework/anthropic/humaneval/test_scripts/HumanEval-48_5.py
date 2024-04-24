def is_palindrome(text: str) -> bool:
    """
    Checks if the given string is a palindrome.
    
    Args:
        text (str): The input string to check.
    
    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(c for c in text.lower() if c.isalnum())
    
    # Check if the cleaned text is the same as its reverse
    return cleaned_text == cleaned_text[::-1]



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