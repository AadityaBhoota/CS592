def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of the supplied string that is a palindrome.
    - Append to the end of the string the reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:
        return ""

    n = len(string)
    for i in range(n, -1, -1):
        if is_palindrome(string[:n - i]):
            return string + string[i - 1::-1]

    return string[::-1] + string


def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]



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