def check_greater(arr, number):
    max_num = max(arr)
    
    if max_num < number:
        return 'Yes, the entered number is greater than those in the array'
    else:
        return 'No, entered number is less than those in the array'

def check(candidate):
    assert check_greater([1, 2, 3, 4, 5], 4) == False
    assert check_greater([2, 3, 4, 5, 6], 8) == True
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == True

check(check_greater)