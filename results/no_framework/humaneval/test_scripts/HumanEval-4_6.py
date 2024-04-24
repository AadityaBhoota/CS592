from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    
    mean_value = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean_value) for x in numbers) / len(numbers)
    
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