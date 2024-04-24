from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # If input list is empty, return None
        return None
    max_length = 0
    longest_str = ""
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string
    return longest_str

# Test cases
if __name__ == "__main__":
    assert longest([]) == None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'

check(longest)