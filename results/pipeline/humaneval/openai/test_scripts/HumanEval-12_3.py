from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
        strings (List[str]): List of strings
    
    Returns:
        Optional[str]: The longest string in the input list or None if the list is empty
    """
    
    if not strings:
        return None
    
    max_length_str = strings[0]
    
    for string in strings:
        if len(string) > len(max_length_str):
            max_length_str = string
    
    return max_length_str



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == None
    assert candidate(['x', 'y', 'z']) == 'x'
    assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'

check(longest)