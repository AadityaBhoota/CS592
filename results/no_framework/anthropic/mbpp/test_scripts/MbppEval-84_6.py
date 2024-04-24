def sequence(n):
    """
    Find the nth number in the Newman-Conway sequence.
    
    The Newman-Conway sequence is defined as follows:
    - The first two numbers in the sequence are 1 and 1.
    - For n > 2, the nth number is the number of times the (n-1)th number appears in the sequence up to the (n-1)th number.
    
    Args:
        n (int): The index of the desired number in the sequence.
        
    Returns:
        int: The nth number in the Newman-Conway sequence.
    """
    if n == 1 or n == 2:
        return 1
    
    # Initialize the first two numbers in the sequence
    seq = [1, 1]
    
    # Generate the sequence up to the nth number
    for i in range(2, n):
        count = 1
        num = seq[i-1]
        result = []
        for j in range(i-1, -1, -1):
            if seq[j] == num:
                count += 1
            else:
                result.append(count)
                count = 1
                num = seq[j]
        result.append(count)
        result.reverse()
        seq.extend(result)
    
    return seq[n-1]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)