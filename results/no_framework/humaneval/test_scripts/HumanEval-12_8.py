def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    
    max_length = max(len(s) for s in strings)
    longest_string = next(s for s in strings if len(s) == max_length)

    return longest_string



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'

check(longest)