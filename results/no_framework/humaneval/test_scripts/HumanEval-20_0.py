from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    
    min_difference = float('inf')
    closest_pair = None
    
    for i in range(len(numbers) - 1):
        current_difference = numbers[i+1] - numbers[i]
        
        if current_difference < min_difference:
            min_difference = current_difference
            closest_pair = (numbers[i], numbers[i+1])
    
    return closest_pair

# Test cases





METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1)


check(find_closest_elements)