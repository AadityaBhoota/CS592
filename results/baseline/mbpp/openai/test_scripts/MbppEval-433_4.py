def check_greater(arr, number):
    if all(num < number for num in arr):
        return 'No, entered number is greater than those in the array'
    else:
        return 'Yes, the entered number is greater than those in the array'

# Testing the function with the provided examples



def check(candidate):
    assert check_greater([1, 2, 3, 4, 5], 4) == False
    assert check_greater([2, 3, 4, 5, 6], 8) == True
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == True

check(check_greater)