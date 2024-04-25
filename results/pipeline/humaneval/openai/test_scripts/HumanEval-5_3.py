from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    
    for i, num in enumerate(numbers):
        result.append(num)  # Step 3: Append the current number
        if i != len(numbers) - 1:  # Check if it's not the last number
            result.append(delimiter)  # Step 4: Append the delimiter
    
    return result



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]

check(intersperse)