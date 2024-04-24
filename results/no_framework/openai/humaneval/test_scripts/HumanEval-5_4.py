from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    interspersed_list = []
    if len(numbers) < 2:
        return numbers
    for i in range(len(numbers) - 1):
        interspersed_list.append(numbers[i])
        interspersed_list.append(delimiter)
    interspersed_list.append(numbers[-1])
    return interspersed_list

# Test the function with sample inputs
if __name__ == "__main__":
    print(intersperse([], 4))  # Output: []
    print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]

check(intersperse)