def find_Element(arr, ranges, rotations, index):
    def rotate(arr, rotations):
        return arr[-rotations:] + arr[:-rotations]

    for start, end in ranges:
        subarray = arr[start:end+1]
        subarray = rotate(subarray, rotations % len(subarray))
        arr[start:end+1] = subarray

    if index < len(arr):
        return arr[index]
    else:
        return None

# Test cases




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)