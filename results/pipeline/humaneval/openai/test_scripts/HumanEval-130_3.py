def tri(n):
    tribonacci_sequence = [3, 1]  # Initialize the list with the first two values of the Tribonacci sequence
    
    # Iterate from index 2 up to n (inclusive) to calculate the Tribonacci sequence
    for i in range(2, n + 1):
        # Check if i is even or odd to determine the Tribonacci number
        if i % 2 == 0:
            tribonacci_number = 1 + i // 2  # Calculate Tribonacci number for even index i
        else:
            tribonacci_number = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
        
        tribonacci_sequence.append(tribonacci_number)  # Append the calculated Tribonacci number to the list
    
    return tribonacci_sequence

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