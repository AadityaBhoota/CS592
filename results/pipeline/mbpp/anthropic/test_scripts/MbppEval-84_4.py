def sequence(n):
    if n == 1:
        return 1
    else:
        return 1 + sequence(sequence(n-1))

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)