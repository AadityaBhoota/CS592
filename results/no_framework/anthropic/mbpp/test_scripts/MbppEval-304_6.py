def find_Element(arr, ranges, rotations, index):
    # Perform the rotations
    for r in range(rotations):
        for start, end in ranges:
            arr[start:end+1] = arr[start:end+1][::-1]

    # Return the element at the given index
    return arr[index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)