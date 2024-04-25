def decimal_to_binary(n):
    """
    Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.

    Examples:
    decimal_to_binary(8) == '1000'
    decimal_to_binary(18) == '10010'
    decimal_to_binary(7) == '111'
    """
    if n == 0:
        return '0'
    
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    return binary.lstrip('0')

def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)