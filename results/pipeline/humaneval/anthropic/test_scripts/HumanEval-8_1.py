from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = 0
    total_product = 1
    
    for num in numbers:
        total_sum += num
        total_product *= num
    
    return total_sum, total_product



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