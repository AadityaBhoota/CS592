from typing import List

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Running the test cases
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['x', 'y', 'z']) == 'xyz'
    assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'

check(concatenate)