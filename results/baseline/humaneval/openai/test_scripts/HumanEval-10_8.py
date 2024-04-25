def make_palindrome(string: str) -> str:
    if not string:
        return ''

    # Function to check if a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]

    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            return string + string[:i-1][::-1]

    return string  # Return the input string if no palindrome suffix is found

# Testing the function with the provided test cases






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