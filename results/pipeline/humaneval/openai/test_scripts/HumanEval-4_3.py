from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Step 1: Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Step 2: Calculate the absolute differences between each element and the mean
    absolute_diffs = [abs(number - mean) for number in numbers]
    
    # Step 3: Calculate the Mean Absolute Deviation (MAD) by averaging the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    # Step 4: Return the Mean Absolute Deviation (MAD)
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