from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    
    absolute_diff = [abs(num - mean) for num in numbers]
    
    mean_abs_dev = sum(absolute_diff) / len(numbers)
    return mean_abs_dev



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


check(mean_absolute_deviation)