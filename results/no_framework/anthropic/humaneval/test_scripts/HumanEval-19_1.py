from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map the words to their corresponding integer values
    word_to_int = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    words = numbers.split()
    
    # Convert the words to their corresponding integer values
    nums = [word_to_int[word] for word in words]
    
    # Sort the integers and convert them back to their corresponding words
    sorted_nums = [list(word_to_int.keys())[list(word_to_int.values()).index(num)] for num in sorted(nums)]
    
    # Join the sorted words back into a string
    return ' '.join(sorted_nums)



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