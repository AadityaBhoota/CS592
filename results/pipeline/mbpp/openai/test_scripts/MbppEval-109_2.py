def odd_Equivalent(s,n): 
    '''
    Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.

    Examples:
    odd_Equivalent("011001",6) == 3
    odd_Equivalent("11011",5) == 4
    odd_Equivalent("1010",4) == 2
    '''
def odd_equivalent(s, n):
    count = 0
    for _ in range(n):
        s = s[-1] + s[:-1]  # Rotate the binary string
        decimal_num = int(s, 2)  # Convert binary string to decimal number
        if decimal_num % 2 != 0:  # Check if decimal number is odd
            count += 1
    return count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)