def generate_binary_sequences(n, sequence=[], prefix_sum=0):
    if len(sequence) == 2*n:
        return [sequence] if prefix_sum == 0 else []
    
    sequences = []
    for bit in [0, 1]:
        new_sequence = sequence + [bit]
        new_prefix_sum = prefix_sum + (-1) ** bit
        sequences += generate_binary_sequences(n, new_sequence, new_prefix_sum)
        
    return sequences

def count_binary_seq(n):
    binary_sequences = generate_binary_sequences(n)
    return len(binary_sequences)

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)