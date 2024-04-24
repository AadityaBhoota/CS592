def even_bit_set_number(n):
    """
    Write a python function to set all even bits of a given number.

    Examples:
    even_bit_set_number(10) == 10
    even_bit_set_number(20) == 30
    even_bit_set_number(30) == 30
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:]

    # Reverse the binary string
    reversed_binary_str = binary_str[::-1]

    # Set all even bits to 1
    even_bits_set_str = ''.join(['1' if i % 2 == 0 else reversed_binary_str[i] for i in range(len(reversed_binary_str))])

    # Reverse the binary string back and convert it to an integer
    result = int(even_bits_set_str[::-1], 2)

    return result

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)