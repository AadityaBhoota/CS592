def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = strings[0]
    max_length = len(strings[0])
    for s in strings[1:]:
        if len(s) > max_length:
            longest_str = s
            max_length = len(s)
    return longest_str

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'

check(longest)