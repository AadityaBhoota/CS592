def find_Element(arr, ranges, rotations, index):
    # Perform rotations on the array elements
    for i in range(rotations):
        start, end = ranges[i]
        arr[start:end+1] = arr[end:start-1:-1]

    # Return the element at the given index
    return arr[index]

# Test cases




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)