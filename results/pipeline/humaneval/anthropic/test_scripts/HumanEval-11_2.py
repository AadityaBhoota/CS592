from typing import List

def string_xor(a: str, b: str) -> str:
    # Convert the input strings to lists of integers
    a_list = [int(char) for char in a]
    b_list = [int(char) for char in b]

    # Perform the XOR operation on the corresponding elements
    result_list = [a_elem ^ b_elem for a_elem, b_elem in zip(a_list, b_list)]

    # Convert the resulting list of integers back to a string
    return ''.join(str(x) for x in result_list)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)