def decimal_to_binary(n):
    binary_num = bin(n)[2:]  # Remove '0b' prefix
    binary_num = binary_num.lstrip('0') if n != 0 else '0'  # Remove leading zeros for non-zero values
    return binary_num

def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)