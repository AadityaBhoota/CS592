from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    
    n = len(numbers)
    mean = sum(numbers) / n
    absolute_deviations = [abs(x - mean) for x in numbers]
    mad = sum(absolute_deviations) / n
    
    return mad

# Test the function




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


check(mean_absolute_deviation)