def string_sequence(n: int) -> str:
    sequence = ''
    
    for num in range(n + 1):
        sequence += str(num) + ' '
    
    sequence = sequence.strip()
    
    return sequence



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'

check(string_sequence)