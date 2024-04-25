from typing import List

def sort_numbers(numbers: str) -> str:
    number_list = numbers.split()

    num_to_int = {
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

    int_list = [num_to_int[num] for num in number_list]
    sorted_int_list = sorted(int_list)

    int_to_num = {value: key for key, value in num_to_int.items()}
    sorted_number_list = [int_to_num[num] for num in sorted_int_list]

    sorted_numbers = ' '.join(sorted_number_list)

    return sorted_numbers



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