def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of the supplied string that is a palindrome.
    - Append to the end of the string a reverse of a string prefix that comes before the palindromic suffix.
    
    Examples:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if string == "":
        return ""
    
    def find_longest_palindrome_suffix(s):
        for i in range(len(s), 0, -1):
            if is_palindrome(s[:i]):
                return s[i:]
    
    longest_palindrome_suffix = find_longest_palindrome_suffix(string)
    return string + string[:len(string)-len(longest_palindrome_suffix)][::-1]


# Test cases






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