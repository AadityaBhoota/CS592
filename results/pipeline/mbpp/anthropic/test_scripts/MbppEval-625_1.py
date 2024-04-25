def swap_List(new_list):
    first = new_list[0]
    last = new_list[-1]
    new_list[0] = last
    new_list[-1] = first
    return new_list

def check(candidate):
    assert swap_List([1,2,3]) == [3,2,1]
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
    assert swap_List([4,5,6]) == [6,5,4]

check(swap_List)