from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    sorted_numbers = sorted(numbers)

    closest_pair = None
    closest_distance = float('inf')

    for i in range(len(sorted_numbers) - 1):
        distance = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if distance < closest_distance:
            closest_distance = distance
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair



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