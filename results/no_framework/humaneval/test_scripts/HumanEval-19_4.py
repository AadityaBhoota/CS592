def sort_numbers(numbers: str) -> str:
    numberals = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    # Create a dictionary to map numberals to their numerical value
    number_dict = {numberal: index for index, numberal in enumerate(numberals)}
    
    # Split the input string and sort based on the numerical value
    sorted_numbers = sorted(numbers.split(), key=lambda x: number_dict[x])
    
    return ' '.join(sorted_numbers)



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