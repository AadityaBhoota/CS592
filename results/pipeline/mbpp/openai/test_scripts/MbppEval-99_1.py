def decimal_to_binary(n):
    binary_str = bin(n)[2:]  # Remove '0b' prefix
    binary_str = binary_str.zfill(4)  # Left-pad with zeros to ensure a minimum length of 4 characters
    return binary_str

def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)