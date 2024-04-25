def second_smallest(numbers):
    if len(numbers) < 2:
        return None

    smallest = min(numbers)
    second_smallest = None

    for num in numbers:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num

    return second_smallest

def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)