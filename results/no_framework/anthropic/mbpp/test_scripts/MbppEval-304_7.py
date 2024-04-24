def find_Element(arr, ranges, rotations, index):
    """
    Write a Python function to find the element at a given index after a number of rotations.

    Args:
        arr (list): The original array.
        ranges (list): A list of ranges, where each range is represented as a list of two indices [start, end].
        rotations (int): The number of rotations to perform.
        index (int): The index of the element to find.

    Returns:
        The element at the given index after the rotations.
    """
    # Perform the rotations
    for _ in range(rotations):
        for range_start, range_end in ranges:
            arr[range_start:range_end+1] = arr[range_start:range_end+1][::-1]

    # Return the element at the given index
    return arr[index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)