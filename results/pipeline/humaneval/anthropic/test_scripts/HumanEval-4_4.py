from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    abs_diffs = [abs(num - mean) for num in numbers]
    mad = sum(abs_diffs) / len(abs_diffs)
    return mad



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


check(mean_absolute_deviation)