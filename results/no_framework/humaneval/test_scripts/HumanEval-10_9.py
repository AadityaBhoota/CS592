def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    def is_palindrome(string: str) -> bool:
        return string == string[::-1]
    
    if not string:
        return ''
    
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            return string + string[:-i][::-1]

# Testing the function
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'



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