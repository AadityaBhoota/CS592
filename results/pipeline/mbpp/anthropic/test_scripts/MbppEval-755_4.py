def second_smallest(numbers):
    if not numbers:
        return None

    smallest = numbers[0]
    second_smallest = numbers[0]

    for num in numbers[1:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num > smallest:
            second_smallest = num

    return second_smallest

def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)