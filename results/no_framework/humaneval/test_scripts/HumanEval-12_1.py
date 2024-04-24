from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    max_length = max(len(s) for s in strings)
    longest_strings = [s for s in strings if len(s) == max_length]

    return longest_strings[0]

# Testing the function






METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'

check(longest)