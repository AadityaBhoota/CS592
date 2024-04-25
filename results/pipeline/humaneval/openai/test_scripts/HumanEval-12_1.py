from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    
    max_len = 0
    longest_str = None
    
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            longest_str = string
        elif len(string) == max_len and longest_str is None:
            longest_str = string

    return longest_str



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'

check(longest)