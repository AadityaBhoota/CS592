def is_Diff(n):
    """
    Write a python function to find whether a number is divisible by 11.

    Examples:
    is_Diff(12345) == False
    is_Diff(1212112) == True
    is_Diff(1212) == False
    """
    sum1 = 0
    sum2 = 0
    n_str = str(n)
    for i, digit in enumerate(n_str):
        if i % 2 == 0:
            sum1 += int(digit)
        else:
            sum2 += int(digit)
    diff = abs(sum1 - sum2)
    return diff % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)