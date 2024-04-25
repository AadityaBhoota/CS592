from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Step 0: Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Step 1: Calculate the absolute deviation for each element
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Step 2: Calculate the mean of the absolute deviations
    mean_absolute_deviation = sum(absolute_deviations) / len(absolute_deviations)
    
    return mean_absolute_deviation



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


check(mean_absolute_deviation)