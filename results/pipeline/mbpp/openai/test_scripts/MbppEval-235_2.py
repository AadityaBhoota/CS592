def even_bit_set_number(n):
    # Step 0: Convert the given number to binary
    binary_n = bin(n)[2:]

    # Step 1: Initialize a mask to set all even bits to 1 in binary (10 in binary)
    mask = int(''.join(['10' * (len(binary_n)//2)]), 2)

    # Step 2: Perform a bitwise OR operation between the number and the mask to set all even bits
    result = n | mask

    return result

# Test the function




def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30

check(even_bit_set_number)