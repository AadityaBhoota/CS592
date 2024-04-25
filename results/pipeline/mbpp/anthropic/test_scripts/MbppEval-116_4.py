def tuple_to_int(nums):
    result = ""
    for num in nums:
        result += str(num)
    return int(result)

def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567

check(tuple_to_int)