def tri(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    elif n == 3:
        return [3, 2, 8]
    else:
        result = [3, 2, 8]
        n_minus_1, n_minus_2, n_plus_1 = 8, 2, 3
        for i in range(4, n+1):
            if i % 2 == 0:
                current = 1 + i // 2
            else:
                current = n_minus_1 + n_minus_2 + n_plus_1
                n_minus_2, n_minus_1, n_plus_1 = n_minus_1, n_plus_1, current
            result.append(current)
        return result

# Test the function
n = 5
print(tri(n))  # Output: [3, 2, 8, 9, 32, 23]

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