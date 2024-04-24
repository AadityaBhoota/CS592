def decimal_to_binary(n):
    """
    Convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.

    Examples:
    decimal_to_binary(8) == '1000'
    decimal_to_binary(18) == '10010'
    decimal_to_binary(7) == '111'
    """
    binary_str = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
    return binary_str

def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)