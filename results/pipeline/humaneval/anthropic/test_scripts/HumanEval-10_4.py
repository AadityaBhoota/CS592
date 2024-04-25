def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    """
    if not string:
        return ""
    
    longest_palindromic_suffix = find_longest_palindromic_suffix(string)
    prefix_to_reverse = string[:-len(longest_palindromic_suffix)]
    reversed_prefix = prefix_to_reverse[::-1]
    
    return string + reversed_prefix

def find_longest_palindromic_suffix(string: str) -> str:
    """
    Find the longest palindromic suffix of the given string.
    """
    n = len(string)
    s = "#" + "#".join(string) + "#"
    length = len(s)
    p = [0] * length
    
    center, right_boundary = 0, 0
    for i in range(1, length):
        if i <= right_boundary:
            p[i] = min(right_boundary - i + 1, p[2 * center - i])
        
        while i - p[i] >= 0 and i + p[i] < length and s[i - p[i]] == s[i + p[i]]:
            p[i] += 1
        
        if i + p[i] - 1 > right_boundary:
            center, right_boundary = i, i + p[i] - 1
    
    max_len = max(p)
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    end = start + max_len
    return string[start:end]

def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome.
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