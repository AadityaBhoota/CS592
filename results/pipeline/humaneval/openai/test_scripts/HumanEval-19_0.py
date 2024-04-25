def sort_numbers(numbers: str) -> str:
    number_words = numbers.split()
    
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    sorted_number_words = sorted(number_words, key=lambda x: number_map[x])
    sorted_numbers_str = ' '.join(sorted_number_words)
    
    return sorted_numbers_str



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'

check(sort_numbers)