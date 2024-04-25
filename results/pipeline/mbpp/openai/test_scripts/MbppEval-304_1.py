def find_Element(arr, ranges, rotations, index):
    total_rotations = sum([r[1] for r in ranges]) * rotations
    effective_index = (index + total_rotations) % len(arr)
    return arr[effective_index]

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)