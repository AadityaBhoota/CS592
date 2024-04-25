from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference of each number from the mean
    absolute_diff = [abs(num - mean) for num in numbers]
    
    # Calculate the average of these absolute differences
    mean_absolute_dev = sum(absolute_diff) / len(absolute_diff)
    return mean_absolute_dev



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


check(mean_absolute_deviation)