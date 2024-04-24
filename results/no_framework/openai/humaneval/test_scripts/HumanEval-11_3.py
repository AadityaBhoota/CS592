def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Strings a and b must have the same length")

    result = ""
    for char1, char2 in zip(a, b):
        if char1 == char2:
            result += "0"
        else:
            result += "1"
    
    return result

# Test the function




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)