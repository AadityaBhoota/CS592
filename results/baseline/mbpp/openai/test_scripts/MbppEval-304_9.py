def find_Element(arr, ranges, rotations, index):
    for l, r in ranges:
        for i in range(l, r+1):
            index_shift = 0
            for _ in range(rotations):
                index_shift += 1
                if index == i:
                    index = l + ((i - l + index_shift) % (r - l + 1))
                if index == l:
                    index = r
    return arr[index]

# Examples




def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

check(find_Element)