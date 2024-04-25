def sequence(n): 
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    seq = [0, 1, 1]  # Initialize with the base cases
    
    for i in range(3, n+1):
        seq.append(seq[seq[i-1]] + seq[i - seq[i-1]])
    
    return seq[n]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)