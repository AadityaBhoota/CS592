def odd_Equivalent(s,n): 
    '''
    Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.

    Examples:
    odd_Equivalent("011001",6) == 3
    odd_Equivalent("11011",5) == 4
    odd_Equivalent("1010",4) == 2
    '''
def odd_equivalent(binary_string, n):
    rotated_string = binary_string[-n % len(binary_string):] + binary_string[:-n % len(binary_string)]
    count = sum(1 for char in rotated_string if int(char) % 2 != 0)
    return count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)