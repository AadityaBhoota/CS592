def make_palindrome(string: str) -> str:
    if not string:
        return ""

    s = string + "#" + string[::-1]
    prefix_table = build_prefix_table(s)
    longest_palindromic_prefix = s[: prefix_table[-1]]
    return string + longest_palindromic_prefix[len(string):]

def build_prefix_table(s: str) -> list[int]:
    prefix_table = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = prefix_table[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix_table[i] = j
    return prefix_table



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