def tuple_to_int(nums):
    num_str = ''.join(map(str, nums))
    return int(num_str)

# Test the function with the provided examples




def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567

check(tuple_to_int)