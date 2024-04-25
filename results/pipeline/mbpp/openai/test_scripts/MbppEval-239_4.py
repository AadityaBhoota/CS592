def generate_sequences(m, n, sequence=[], start=1):
    if len(sequence) == n:
        return [sequence]
    sequences = []
    for i in range(start, m+1):
        sequences.extend(generate_sequences(m, n, sequence + [i], 2*i))
    return sequences

def get_total_number_of_sequences(m, n):
    def helper(m, n, sequence=[], start=1):
        if len(sequence) == n:
            return [sequence]
        sequences = []
        for i in range(start, m+1):
            sequences.extend(helper(m, n, sequence + [i], 2 * i))
        return sequences
    
    valid_sequences = [sequence for sequence in helper(m, n) if all(sequence[i] >= 2 * sequence[i-1] for i in range(1, len(sequence)))]
    return len(valid_sequences)

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)