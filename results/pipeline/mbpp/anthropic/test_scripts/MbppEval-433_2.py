def check_greater(arr, number):
    greater_count = 0
    for element in arr:
        if element < number:
            greater_count += 1
    
    if greater_count == len(arr):
        return "Yes, the entered number is greater than those in the array"
    else:
        return "No, the entered number is not greater than those in the array"

def check(candidate):
    assert check_greater([1, 2, 3, 4, 5], 4) == False
    assert check_greater([2, 3, 4, 5, 6], 8) == True
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == True

check(check_greater)