def sequence(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return sequence(sequence(n - 1)) + sequence(n - sequence(n - 1))

# Test the function




def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)