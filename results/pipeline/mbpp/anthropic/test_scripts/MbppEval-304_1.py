def find_Element(arr, ranges, rotations, index):
    for start, end in ranges:
        arr = rotate_array(arr[start:end+1], rotations) + arr[:start] + arr[end+1:]
    return arr[index]

def rotate_array(arr, k):
    return arr[-k:] + arr[:-k]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)