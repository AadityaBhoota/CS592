def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length")

    result = ''
    for bit_a, bit_b in zip(a, b):
        result += str(int(bit_a) ^ int(bit_b))

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