def find_First_Missing(array, start=0, end=None):
    missing_num = 0

    for i in range(start, end):
        if array[i] != missing_num:
            return missing_num
        
        missing_num += 1
    
    return missing_num

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)