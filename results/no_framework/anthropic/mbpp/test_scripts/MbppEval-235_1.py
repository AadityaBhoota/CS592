def even_bit_set_number(n):
    """
    Write a Python function to set all even bits of a given number.

    Examples:
    even_bit_set_number(10) == 10
    even_bit_set_number(20) == 30
    even_bit_set_number(30) == 30
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:]

    # Iterate through the binary string and set the even bits to 1
    new_binary_str = ''.join(['1' if i % 2 == 0 else binary_str[i] for i in range(len(binary_str))])

    # Convert the modified binary string back to an integer
    return int(new_binary_str, 2)

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)