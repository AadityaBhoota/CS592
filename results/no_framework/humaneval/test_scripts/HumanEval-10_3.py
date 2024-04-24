def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    def find_longest_palindromic_suffix(s: str) -> str:
        for i in range(len(s), 0, -1):
            if is_palindrome(s[:i]):
                return s[i:]
        return s

    if not string:
        return ''
    
    longest_suffix = find_longest_palindromic_suffix(string)
    prefix = string[:len(string) - len(longest_suffix)]
    
    return string + prefix[::-1]



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