def cube_nums(nums):
    """
    Write a function to find cubes of individual elements in a list.

    Examples:
    cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    cube_nums([10,20,30]) == [1000, 8000, 27000]
    cube_nums([12,15]) == [1728, 3375]
    """
    return [num ** 3 for num in nums]

def check(candidate):
    assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    assert cube_nums([10,20,30])==([1000, 8000, 27000])
    assert cube_nums([12,15])==([1728, 3375])

check(cube_nums)