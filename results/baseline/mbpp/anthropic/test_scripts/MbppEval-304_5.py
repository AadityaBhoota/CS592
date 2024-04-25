def find_Element(arr, ranges, rotations, index):
    """
    Write a Python function to find the element at a given index after a number of rotations.

    Args:
        arr (list): The original array.
        ranges (list of lists): A list of ranges, where each range is represented as a list of two indices.
        rotations (int): The number of rotations to perform.
        index (int): The index of the element to find.

    Returns:
        int: The element at the given index after the rotations.
    """
    for _ in range(rotations):
        for start, end in ranges:
            arr = arr[start:end+1] + arr[:start] + arr[end+1:]
    return arr[index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)