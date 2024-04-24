from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the sum of absolute differences
    sum_abs_diff = sum(abs(x - mean) for x in numbers)

    # Calculate the Mean Absolute Deviation
    mad = sum_abs_diff / len(numbers)

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