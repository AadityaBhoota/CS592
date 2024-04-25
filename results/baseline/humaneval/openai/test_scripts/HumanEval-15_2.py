def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    
    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(map(str, range(n+1)))

# Testing the function
if __name__ == "__main__":
    import doctest
    doctest.testmod()



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'

check(string_sequence)