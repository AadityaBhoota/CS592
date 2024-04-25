from typing import List

WORD_TO_INT = {
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

def sort_numbers(numbers: str) -> str:
    word_list = numbers.split()
    int_list = [WORD_TO_INT[word] for word in word_list]
    int_list.sort()
    sorted_words = [next(k for k, v in WORD_TO_INT.items() if v == num) for num in int_list]
    return ' '.join(sorted_words)



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