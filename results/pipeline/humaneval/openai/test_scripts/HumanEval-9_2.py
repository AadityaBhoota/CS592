from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    
    for i in range(len(numbers)):
        if i == 0:
            rolling_max_list.append(numbers[i])
        else:
            max_val = max(numbers[:i+1])
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