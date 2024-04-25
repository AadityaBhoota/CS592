from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    max_length = 0
    longest_string = None

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string

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