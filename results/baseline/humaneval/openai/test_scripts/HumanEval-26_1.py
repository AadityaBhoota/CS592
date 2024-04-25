def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

# Test the function




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

check(remove_duplicates)