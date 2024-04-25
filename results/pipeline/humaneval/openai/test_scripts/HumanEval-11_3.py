def string_xor(a: str, b: str) -> str:
    result = ""
    for i in range(min(len(a), len(b))):  # iterating over the indices of the smaller string
        result += str(int(a[i]) ^ int(b[i]))  # performing XOR operation on the characters
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