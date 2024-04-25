def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the input strings to integers
    a_int = int(a, 2)
    b_int = int(b, 2)

    # Perform XOR operation on the integers
    result_int = a_int ^ b_int

    # Convert the result back to a binary string
    result_str = bin(result_int)[2:]

    return result_str



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)