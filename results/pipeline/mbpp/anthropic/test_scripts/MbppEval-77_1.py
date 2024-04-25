def is_Diff(n):
    """
    Write a python function to find whether a number is divisible by 11.

    Examples:
    is_Diff(12345) == False
    is_Diff(1212112) == True
    is_Diff(1212) == False
    """
    num_str = str(n)
    odd_sum = 0
    even_sum = 0
    for i, digit in enumerate(num_str):
        if i % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    diff = abs(odd_sum - even_sum)
    return diff % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)