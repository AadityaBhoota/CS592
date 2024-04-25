def multiply_elements(test_tup):
    """
    Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.

    Examples:
    multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
    multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
    multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
    """
    result = []
    for i in range(len(test_tup) - 1):
        result.append(test_tup[i] * test_tup[i+1])
    return tuple(result)

def check(candidate):
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
    assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
    assert multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
    assert multiply_elements((12,)) == ()

check(multiply_elements)