from typing import List

def concatenate(strings: List[str]) -> str:
    concatenated_string = ''
    
    for string in strings:
        concatenated_string += string
    
    return concatenated_string



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['x', 'y', 'z']) == 'xyz'
    assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'

check(concatenate)