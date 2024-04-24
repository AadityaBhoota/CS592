def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Args:
        text (str): The input string to be checked.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    """
    # Remove any whitespace and convert to lowercase
    text = text.lower().replace(" ", "")

    # Check if the string is the same as its reverse
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