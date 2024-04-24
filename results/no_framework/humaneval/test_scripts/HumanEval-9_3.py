from collections import deque
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    window = deque()
    
    for i, num in enumerate(numbers):
        while window and numbers[window[-1]] < num:
            window.pop()
        window.append(i)
        
        if window[0] == i - len(window):
            window.popleft()
        
        result.append(numbers[window[0]])
    
    return result


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]

check(rolling_max)