def string_xor(a: str, b: str) -> str:
    result = ''
    for char1, char2 in zip(a, b):
        if char1 != char2:
            result += '1'
        else:
            result += '0'
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