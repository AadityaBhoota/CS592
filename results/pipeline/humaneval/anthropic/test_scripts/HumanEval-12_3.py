from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest_str):
            longest_str = s
        elif len(s) == len(longest_str):
            # Keep longest_str as is to preserve the first longest string
            pass

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