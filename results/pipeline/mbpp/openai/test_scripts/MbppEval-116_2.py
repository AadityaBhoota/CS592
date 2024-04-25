def tuple_to_int(nums):
    int_str = ''
    
    for num in nums:
        int_str += str(num)
    
    return int(int_str)

def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567

check(tuple_to_int)