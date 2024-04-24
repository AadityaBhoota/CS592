def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")

    result = ""
    for char_a, char_b in zip(a, b):
        if char_a == char_b:
            result += "0"
        else:
            result += "1"

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1101'))  # Output: '0111'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)