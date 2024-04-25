from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_elements = []
    seen = set()

    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_elements.append(num)

    return unique_elements



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

check(remove_duplicates)