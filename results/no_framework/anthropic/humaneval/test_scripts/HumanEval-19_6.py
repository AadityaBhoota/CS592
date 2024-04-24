from typing import List

NUMERAL_TO_INT = {
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
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numerals
    numerals = numbers.split()

    # Convert the numerals to their corresponding integer values
    integer_values = [NUMERAL_TO_INT[numeral] for numeral in numerals]

    # Sort the integer values in ascending order
    integer_values.sort()

    # Convert the sorted integer values back to their corresponding numerals
    sorted_numerals = [list(NUMERAL_TO_INT.keys())[list(NUMERAL_TO_INT.values()).index(value)] for value in integer_values]

    # Join the sorted numerals into a space-delimited string
    return ' '.join(sorted_numerals)



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