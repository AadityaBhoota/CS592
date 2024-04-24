def make_palindrome(string: str) -> str:
    if not string:
        return ''

    # Function to check if a string is a palindrome
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            break

    # Append to the end of the string reverse of a string prefix before the palindromic suffix
    return string + string[:len(string) - i][::-1]

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