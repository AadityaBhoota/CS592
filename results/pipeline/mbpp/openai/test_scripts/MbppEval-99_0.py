def decimal_to_binary(n): 
    binary_digits = []
    
    while n > 0:
        binary_digits.append(str(n % 2))
        n = n // 2
        
    binary_digits.reverse()
    binary_string = ''.join(binary_digits)
    return binary_string

def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'

check(decimal_to_binary)