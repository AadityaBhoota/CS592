from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if numbers.count(num) == 1]


# Test the function




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

check(remove_duplicates)