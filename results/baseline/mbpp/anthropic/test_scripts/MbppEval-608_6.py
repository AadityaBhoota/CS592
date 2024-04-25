def bell_Number(n): 
    '''
    Write a python function to find nth bell number.

    Examples:
    bell_Number(2) == 2
    bell_Number(3) == 5
    bell_Number(4) == 15
    '''
def bell_number(n):
    """
    Calculate the nth Bell number.

    The Bell number B(n) is the number of ways a set of n distinct elements can
    be partitioned into non-empty subsets.

    Args:
        n (int): The index of the Bell number to calculate.

    Returns:
        int: The nth Bell number.
    """
    if n == 0:
        return 1
    if n == 1:
        return 1

    bell_table = [0] * (n + 1)
    bell_table[0] = 1
    bell_table[1] = 1

    for i in range(2, n + 1):
        for j in range(i - 1, -1, -1):
            bell_table[i] += bell_table[j] * (i - j)

    return bell_table[n]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)