from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1

    total_sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num

    return total_sum, product


# Testing the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)



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