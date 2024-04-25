def count_binary_seq(n):
    def generate_binary_sequences(n):
        if n == 0:
            return ['']
        
        prev_sequences = generate_binary_sequences(n - 1)
        new_sequences = []
        
        for seq in prev_sequences:
            new_sequences.append(seq + '0')
            new_sequences.append(seq + '1')
        
        return new_sequences

    def calculate_sums(seq, n):
        first_half = seq[:n]
        last_half = seq[n:]
        
        sum_first_half = sum(int(bit) for bit in first_half)
        sum_last_half = sum(int(bit) for bit in last_half)
        
        return sum_first_half, sum_last_half

    def count_equal_sums(n):
        sequences = generate_binary_sequences(n)
        count = 0
        
        for seq in sequences:
            sum_first_half, sum_last_half = calculate_sums(seq, n)
            if sum_first_half == sum_last_half:
                count += 1
        
        return count
    
    return count_equal_sums(n)

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)