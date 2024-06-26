from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary to map the number words to their corresponding integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    number_words = numbers.split()
    
    # Convert the number words to their corresponding integer values
    number_values = [number_map[word] for word in number_words]
    
    # Sort the integer values
    number_values.sort()
    
    # Convert the sorted integer values back to number words
    sorted_words = [next(key for key, value in number_map.items() if value == num) for num in number_values]
    
    # Join the sorted number words and return the result
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