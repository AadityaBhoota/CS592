def second_smallest(numbers):
    if not numbers:
        return None
    
    smallest = None
    second_smallest = None
    
    for num in numbers:
        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or (num > smallest and num < second_smallest):
            second_smallest = num
    
    return second_smallest if second_smallest is not None else None

def check(candidate):
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert second_smallest([2,2])==None
    assert second_smallest([2,2,2])==None

check(second_smallest)