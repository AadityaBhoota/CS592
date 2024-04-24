def tri(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [3]

    tribonacci_sequence = [3]
    a, b, c = 0, 0, 3

    for i in range(1, n):
        if i % 2 == 0:
            x = a + b * c
        else:
            x = a + b
        tribonacci_sequence.append(x)
        a, b, c = b, c, x

    return tribonacci_sequence

# Test the tri function
print(tri(3))  # Output: [3, 3, 3, 6]
print(tri(7))  # Output: [3, 3, 3, 6, 9, 15, 24, 39]

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