from typing import List, Tuple
from functools import reduce
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1

    # Sum of all integers in the list
    total_sum = sum(numbers)

    # Product of all integers in the list using functools.reduce
    total_product = reduce(operator.mul, numbers, 1)

    return total_sum, total_product

# Testing the function





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