from typing import List

def string_xor(a: str, b: str) -> str:
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    xor_result = int_a ^ int_b
    
    xor_result_str = bin(xor_result)[2:]

    return xor_result_str



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)