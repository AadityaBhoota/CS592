from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_of_numbers = 0
    product_of_numbers = 1

    for number in numbers:
        sum_of_numbers += number
        product_of_numbers *= number

    return sum_of_numbers, product_of_numbers



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