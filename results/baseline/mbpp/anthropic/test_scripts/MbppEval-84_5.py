def sequence(n):
    """
    Find the nth number in the Newman-Conway sequence.

    The Newman-Conway sequence is defined as follows:
    - The first two numbers are 1 and 1.
    - For n > 2, the nth number is the smallest positive integer that is not yet in the sequence and can be written as the sum of two earlier terms in the sequence.

    Args:
        n (int): The index of the number to find in the sequence.

    Returns:
        int: The nth number in the Newman-Conway sequence.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1 or n == 2:
        return 1

    sequence = [1, 1]
    i = 2
    while len(sequence) < n:
        candidate = min(x + y for x in sequence for y in sequence if x <= y)
        if candidate not in sequence:
            sequence.append(candidate)
        i += 1

    return sequence[n - 1]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)