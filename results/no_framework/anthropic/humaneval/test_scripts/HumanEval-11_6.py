from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the input strings to lists of integers
    a_list = [int(char) for char in a]
    b_list = [int(char) for char in b]

    # Perform XOR operation
    result_list = [str(x ^ y) for x, y in zip(a_list, b_list)]

    # Convert the result back to a string
    return ''.join(result_list)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)