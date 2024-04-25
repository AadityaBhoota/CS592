def odd_position(nums):
    result = True
    for i in range(1, len(nums), 2):  # Loop through odd indices starting from index 1
        if nums[i] % 2 == 0:  # Check if the number at the odd index is even
            result = False
            break
    return result

def check(candidate):
    assert odd_position([2,1,4,3,6,7,6,3]) == True
    assert odd_position([4,1,2]) == True
    assert odd_position([1,2,3]) == False

check(odd_position)