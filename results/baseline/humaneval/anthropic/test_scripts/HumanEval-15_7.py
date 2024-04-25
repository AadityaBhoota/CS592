def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.
    
    Returns:
        str: A string containing the sequence of numbers.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    sequence = [str(i) for i in range(n + 1)]
    return ' '.join(sequence)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'

check(string_sequence)