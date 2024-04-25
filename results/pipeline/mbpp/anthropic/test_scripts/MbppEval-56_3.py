def get_reverse(n):
    """
    Helper function to get the reverse of a number.
    """
    return int(str(n)[::-1])

def rev(num):
    """
    Write a python function to check if a given number is one less than twice its reverse.

    Examples:
    check(70) == False
    check(23) == False
    check(73) == True
    """
    reverse_num = get_reverse(num)
    return num == 2 * reverse_num - 1

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True

check(rev)