def second_smallest(numbers):
    if len(numbers) < 2:
        return None

    first_min = min(numbers[0], numbers[1])
    second_min = max(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        if numbers[i] < first_min:
            second_min = first_min
            first_min = numbers[i]
        elif numbers[i] < second_min and numbers[i] != first_min:
            second_min = numbers[i]

    return second_min

def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)