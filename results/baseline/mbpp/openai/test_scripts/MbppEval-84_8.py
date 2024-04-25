def sequence(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        sequence_list = [0] * (n+1)
        sequence_list[1] = 1
        sequence_list[2] = 1
        for i in range(3, n+1):
            sequence_list[i] = sequence_list[sequence_list[i-1]] + sequence_list[i-sequence_list[i-1]]
        return sequence_list[n]

# Test the function with given examples




def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)