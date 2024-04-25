def newman_conway_sequence(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    sequence = [0, 1, 1]  # Initialize the sequence with the first two numbers

    for i in range(3, n + 1):
        sequence.append(sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]])
    
    return sequence[1:]  # Exclude the first element (0) when returning

def sequence(n):
    sequence = newman_conway_sequence(n)
    
    if n <= 0 or n > len(sequence):
        return None
    
    return sequence[n - 1]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)