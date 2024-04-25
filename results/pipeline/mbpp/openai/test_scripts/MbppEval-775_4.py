def odd_position(nums):
    result = True  # Step 2
    for i in range(1, len(nums), 2):  # Step 3
        if nums[i] % 2 == 0:
            result = False
            break  # Step 4
    return result  # Step 5

def check(candidate):
    assert odd_position([2,1,4,3,6,7,6,3]) == True
    assert odd_position([4,1,2]) == True
    assert odd_position([1,2,3]) == False

check(odd_position)