from typing import List

def sort_numbers(numbers: str) -> str:
    numbers_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    numbers_list = numbers.split()
    sorted_numbers = sorted([numbers_dict[num] for num in numbers_list])
    sorted_number_strings = [key for key, value in numbers_dict.items() if value in sorted_numbers]
    
    return ' '.join(sorted_number_strings)



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