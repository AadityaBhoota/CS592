from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    >>> string_xor('010', '110')
    '100'
    """
    
    # Check input
    if not all(c in '01' for c in a) or not all(c in '01' for c in b):
        raise ValueError("Input strings must consist only of '0' and '1'")
    
    # Perform XOR using zip() and a list comprehension
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)