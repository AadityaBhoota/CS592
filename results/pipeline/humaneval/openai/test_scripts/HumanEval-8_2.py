from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Check if numbers list is empty
        return (0, 1)
    
    # Calculate sum and product of numbers in the list
    numbers_sum = sum(numbers)
    numbers_product = 1
    for num in numbers:
        numbers_product *= num
    
    return (numbers_sum, numbers_product)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == (0, 1)
    assert candidate([1, 1, 1]) == (3, 1)
    assert candidate([100, 0]) == (100, 0)
    assert candidate([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
    assert candidate([10]) == (10, 10)

check(sum_product)