from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    current_max = numbers[0]
    result = [current_max]

    for number in numbers[1:]:
        current_max = max(current_max, number)
        result.append(current_max)

    return result

# Testing the function with the given example
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