def decimal_to_binary(n):
    if n < 0:
        return 'Error: Input number should be a non-negative integer.'
    elif n == 0:
        return '0'
    
    binary_digits = []
    
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    
    binary_digits.reverse()

    return ''.join(binary_digits)



def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)