def tuple_to_int(nums):
    num_str = [str(num) for num in nums]
    combined_str = ''.join(num_str)
    final_int = int(combined_str)
    return final_int

def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567

check(tuple_to_int)