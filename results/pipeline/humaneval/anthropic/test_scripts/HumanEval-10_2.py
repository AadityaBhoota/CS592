def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # If the string is already a palindrome, return it
    if is_palindrome(string):
        return string

    # Find the longest palindromic suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            suffix = string[i:]
            break
    else:
        suffix = ''

    # Get the prefix that comes before the palindromic suffix
    prefix = string[:-len(suffix)]

    # Append the reversed prefix to the original string
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