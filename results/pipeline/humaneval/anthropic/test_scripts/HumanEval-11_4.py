from typing import List

def string_xor(a: str, b: str) -> str:
    if not all(c in '01' for c in a) or not all(c in '01' for c in b):
        raise ValueError("Input strings must contain only '1's and '0's.")

    result = ''.join('1' if a_char != b_char else '0' for a_char, b_char in zip(a, b))
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