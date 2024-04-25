def tuple_to_int(nums):
    result = 0
    for num in nums:
        result = result * 10 + num
    return result

def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567

check(tuple_to_int)