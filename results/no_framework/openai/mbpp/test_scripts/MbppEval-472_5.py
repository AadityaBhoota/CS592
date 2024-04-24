def check_Consecutive(l): 
    if len(l) < 2:
        return False
​
    sorted_list = sorted(set(l))
    return sorted_list == list(range(sorted_list[0], sorted_list[-1] + 1))

def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False

check(check_Consecutive)