def sequence(n):
    """
    Write a function to find the nth number in the newman conway sequence.

    Examples:
    sequence(10) == 6
    sequence(2) == 1
    sequence(3) == 2
    """
    seq = [1, 1]
    for i in range(2, n):
        seq.append(bin(seq[-1]).count('1'))
    return seq[n - 1]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)