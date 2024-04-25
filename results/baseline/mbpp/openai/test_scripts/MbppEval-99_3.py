def decimal_to_binary(n):
    if n == 0:
        return '0'
    
    binary_string = ''
    while n > 0:
        binary_string = str(n % 2) + binary_string
        n = n // 2
    
    return binary_string

def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)