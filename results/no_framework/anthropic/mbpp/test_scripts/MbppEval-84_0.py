def sequence(n):
    """
    Write a function to find the nth number in the newman conway sequence.

    Examples:
    sequence(10) == 6
    sequence(2) == 1
    sequence(3) == 2
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    a = [1, 1]
    for i in range(2, n):
        next_num = a[a[-1] - 1] + 1
        a.append(next_num)
    
    return a[-1]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)