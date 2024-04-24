def sequence(n):
    """
    Write a function to find the nth number in the Newman-Conway sequence.

    Examples:
    sequence(10) == 6
    sequence(2) == 1
    sequence(3) == 2
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence(sequence(n - 1))

# Examples




def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)