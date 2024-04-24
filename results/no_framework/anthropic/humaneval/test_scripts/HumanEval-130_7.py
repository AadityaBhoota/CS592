def tri(n):
    """
    Returns the first n + 1 numbers of the Tribonacci sequence.

    Args:
        n (int): The number of Tribonacci numbers to generate.

    Returns:
        list: The first n + 1 Tribonacci numbers.
    """
    if n == 0:
        return [3]
    elif n == 1:
        return [3, 2]
    elif n == 2:
        return [3, 2, 8]

    tribonacci = [3, 2, 8]
    for i in range(3, n + 1):
        if i % 2 == 0:
            next_num = 1 + i // 2
        else:
            next_num = tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
        tribonacci.append(next_num)

    return tribonacci

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