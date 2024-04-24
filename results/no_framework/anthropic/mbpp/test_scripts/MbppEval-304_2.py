def find_Element(arr, ranges, rotations, index):
    """
    Finds the element at the given index after applying the specified number of rotations.

    Args:
        arr (list): The input array.
        ranges (list): A list of ranges (start and end index) to be rotated.
        rotations (int): The number of rotations to be applied.
        index (int): The index of the element to be found.

    Returns:
        int: The element at the specified index after the rotations.
    """
    for _ in range(rotations):
        for start, end in ranges:
            arr[start:end+1] = arr[start:end+1][::-1]

    return arr[index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)