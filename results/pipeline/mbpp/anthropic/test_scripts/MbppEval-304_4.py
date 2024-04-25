def find_Element(arr, ranges, rotations, index):
    current_arr = arr.copy()

    for start, end in ranges:
        current_arr[start:end+1] = current_arr[start:end+1][rotations:] + current_arr[start:end+1][:rotations]

    return current_arr[index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)