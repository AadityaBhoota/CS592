def find_Element(arr, ranges, rotations, index):
    """
    Write a python function to find the element at a given index after a number of rotations.

    Args:
        arr (list): The original array.
        ranges (list): A list of lists, where each inner list represents a range of indices to rotate.
        rotations (int): The number of times the array should be rotated.
        index (int): The index of the element to be found.

    Returns:
        The element at the given index after the specified number of rotations.
    """
    for _ in range(rotations):
        for r in ranges:
            arr[r[0]:r[1]+1] = arr[r[0]:r[1]+1][::-1]
    return arr[index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)