def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of the substring prefix that comes before the palindromic suffix.
    """
    if not string:
        return ''
    
    # Find the longest postfix that is a palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            break
    
    # Append the reverse of the substring prefix that comes before the palindromic suffix
    return string + string[:len(string) - i][::-1]


# Testing the make_palindrome function







METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('x') == 'x'
    assert candidate('xyz') == 'xyzyx'
    assert candidate('xyx') == 'xyx'
    assert candidate('jerry') == 'jerryrrej'

check(make_palindrome)