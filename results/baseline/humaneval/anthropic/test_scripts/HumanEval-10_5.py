def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
    Algorithm idea:
    - Find the longest postfix of the supplied string that is a palindrome.
    - Append to the end of the string the reverse of the string prefix that comes before the palindromic suffix.
    
    Examples:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''
    
    # Find the longest palindromic suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            return string + string[i-1::-1]
    
    # If the entire string is not a palindrome, return the reversed string
    return string[::-1] + string

def is_palindrome(string: str) -> bool:
    """
    Test if a given string is a palindrome.
    """
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