def find_Element(arr, ranges, rotations, index):
    """
    Finds the element at the given index after the specified number of rotations.

    Args:
        arr (list): The input array.
        ranges (list): A list of ranges, each represented as a pair of integers [start, end].
        rotations (int): The number of rotations to perform.
        index (int): The index for which the element is to be found.

    Returns:
        int: The element at the given index after the specified number of rotations.
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