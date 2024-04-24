def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    max_element = numbers[0]
    rolling_max_list = [max_element]
    
    for num in numbers[1:]:
        max_element = max(num, max_element)
        rolling_max_list.append(max_element)
    
    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]

check(rolling_max)