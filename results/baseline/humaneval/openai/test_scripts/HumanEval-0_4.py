from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers
    numbers.sort()
    
    # Iterate through the list and check the difference between adjacent numbers
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] < threshold:
            return True
            
    return False

# Test cases
if __name__ == '__main__':
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False


check(has_close_elements)