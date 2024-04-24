def string_xor(a: str, b: str) -> str:
    result = ''
    for char_a, char_b in zip(a, b):
        result += '1' if char_a != char_b else '0'
    return result


# Test the function with the example provided in the docstring




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)