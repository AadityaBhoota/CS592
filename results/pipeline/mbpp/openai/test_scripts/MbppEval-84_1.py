def sequence(n): 
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    conway_seq = [0, 1, 1]

    for i in range(3, n + 1):
        conway_seq.append(conway_seq[conway_seq[i - 1]] + conway_seq[i - conway_seq[i - 1]])

    return conway_seq[n]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)