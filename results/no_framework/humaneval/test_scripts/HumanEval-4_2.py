from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0

    # Calculate the mean of the numbers
    mean_value = sum(numbers) / len(numbers)

    # Calculate the sum of absolute differences
    sum_abs_diff = sum(abs(x - mean_value) for x in numbers)

    # Calculate the Mean Absolute Deviation
    mean_abs_dev = sum_abs_diff / len(numbers)

    return mean_abs_dev


# Test the function with the example provided
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output should be 1.0



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


check(mean_absolute_deviation)