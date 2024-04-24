from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences from the mean
    absolute_diff = [abs(x - mean) for x in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diff) / len(numbers)
    
    return mad

# Test the function with an example
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


check(mean_absolute_deviation)