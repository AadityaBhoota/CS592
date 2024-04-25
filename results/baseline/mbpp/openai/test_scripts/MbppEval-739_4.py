def find_Index(n):
    index = 1
    triangular_num = 0
    while True:
        triangular_num = index * (index + 1) // 2
        if len(str(triangular_num)) == n:
            return index
        index += 1

# Test cases




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)