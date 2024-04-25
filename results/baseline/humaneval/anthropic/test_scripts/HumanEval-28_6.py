from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    
    Args:
        strings (List[str]): A list of strings.
        
    Returns:
        str: A single string that is the concatenation of all the strings in the input list.
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['x', 'y', 'z']) == 'xyz'
    assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'

check(concatenate)