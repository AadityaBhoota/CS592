def decimal_to_binary(n):
    binary_str = ''
    
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n //= 2
    
    return binary_str or '0'

def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)