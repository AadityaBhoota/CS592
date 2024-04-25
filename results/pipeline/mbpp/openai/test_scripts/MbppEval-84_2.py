def sequence(n): 
    '''
    Find the nth number in the Newman-Conway sequence.

    Examples:
    sequence(10) == 6
    sequence(2) == 1
    sequence(3) == 2
    '''
    if n <= 0:
        return "Invalid input"
    if n == 1 or n == 2:
        return 1

    sequence = [0, 1, 1]  # Initialize with the first two elements of the sequence

    for i in range(3, n+1):
        sequence.append(sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]])

    return sequence[n]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)