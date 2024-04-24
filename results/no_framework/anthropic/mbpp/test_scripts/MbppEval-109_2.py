def odd_Equivalent(s, n):
    """
    Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.

    Examples:
    odd_Equivalent("011001", 6) == 3
    odd_Equivalent("11011", 5) == 4
    odd_Equivalent("1010", 4) == 2
    """
    count = 0
    for _ in range(n):
        s = s[-1] + s[:-1]
        if int(s, 2) % 2 == 1:
            count += 1
    return count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)