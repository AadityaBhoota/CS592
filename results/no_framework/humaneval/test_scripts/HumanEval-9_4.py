from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_list = []  # Initialize an empty list to store rolling max values
    current_max = float('-inf')  # Initialize current_max with negative infinity
    
    for num in numbers:
        current_max = max(current_max, num)  # Update current_max with the maximum of current_max and num
        max_list.append(current_max)  # Append the current_max to the max_list
    
    return max_list

# Test the function with the example input
result = rolling_max([1, 2, 3, 2, 3, 4, 2])




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