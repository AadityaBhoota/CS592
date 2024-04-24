from typing import List

def sort_numbers(numbers: str) -> str:
    # Mapping of number words to numerical values
    number_mapping = {
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

    # Split the input string into individual number words
    number_words = numbers.split()

    # Sort the number words based on their numerical values
    sorted_number_words = sorted(number_words, key=lambda x: number_mapping[x])

    # Join the sorted number words into a single string
    sorted_numbers = ' '.join(sorted_number_words)

    return sorted_numbers

# Test the function with the example input




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