from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    max_val = float('-inf')
    
    for num in numbers:
        max_val = max(max_val, num)
        rolling_max_list.append(max_val)
    
    return rolling_max_list



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