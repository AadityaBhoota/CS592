from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    min_num = min(numbers)
    max_num = max(numbers)
    
    if min_num == max_num:
        return [0.0] * len(numbers)
    
    return [(x - min_num) / (max_num - min_num) for x in numbers]


# Test the function
if __name__ == "__main__":
    input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    output_numbers = rescale_to_unit(input_numbers)
    print(output_numbers)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([2.0, 49.9]) == [0.0, 1.0]
    assert candidate([100.0, 49.9]) == [1.0, 0.0]
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert candidate([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
    assert candidate([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]

check(rescale_to_unit)