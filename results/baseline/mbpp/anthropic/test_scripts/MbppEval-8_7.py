def square_nums(nums):
    """
    Write a function to find squares of individual elements in a list.

    Examples:
    square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    square_nums([10,20,30]) == [100,400,900]
    square_nums([12,15]) == [144,225]
    """
    return [num ** 2 for num in nums]

def check(candidate):
    assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert square_nums([10,20,30])==([100,400,900])
    assert square_nums([12,15])==([144,225])

check(square_nums)