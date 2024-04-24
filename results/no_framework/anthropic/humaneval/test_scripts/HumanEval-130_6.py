def tri(n):
    """
    Returns the first n+1 numbers of the Tribonacci sequence.
    
    The Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n/2, if n is even
    tri(n) = tri(n-1) + tri(n-2) + tri(n+1), if n is odd
    """
    
    # Base case: tri(1) = 3
    if n == 0:
        return [3]
    
    # Initialize the Tribonacci sequence
    tribonacci = [3, 2, 8]
    
    # Compute the rest of the Tribonacci sequence
    for i in range(3, n+1):
        if i % 2 == 0:
            tribonacci.append(1 + i // 2)
        else:
            tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[i-2])
    
    return tribonacci[:n+1]

def check(candidate):

    # Check some simple cases
    
    assert candidate(3) == [1, 3, 2.0, 8.0]
    assert candidate(4) == [1, 3, 2.0, 8.0, 3.0]
    assert candidate(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert candidate(6) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0]
    assert candidate(7) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0]
    assert candidate(8) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0]
    assert candidate(9) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0]
    assert candidate(20) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0, 6.0, 48.0, 7.0, 63.0, 8.0, 80.0, 9.0, 99.0, 10.0, 120.0, 11.0]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(0) == [1]
    assert candidate(1) == [1, 3]

check(tri)