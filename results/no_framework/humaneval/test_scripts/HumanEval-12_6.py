from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest_string) or (len(string) == len(longest_string) and string < longest_string):
            longest_string = string

    return longest_string

# Test cases






METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'

check(longest)