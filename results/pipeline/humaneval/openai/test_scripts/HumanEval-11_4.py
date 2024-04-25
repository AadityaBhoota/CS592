def string_xor(a: str, b: str) -> str:
    # Input Validation
    if not all(char in '01' for char in a) or not all(char in '01' for char in b):
        raise ValueError("Inputs should consist only of 1s and 0s.")

    # Pad the shorter string with zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Perform XOR operation
    result = ''.join(str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b))
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