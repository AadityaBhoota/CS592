def sum_negativenum(nums):
    """
    Write a function to calculate the sum of the negative numbers of a given list of numbers.

    Examples:
    sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
    sum_negativenum([10,15,-14,13,-18,12,-20]) == -52
    sum_negativenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190]) == -894
    """
    negative_sum = 0
    for num in nums:
        if num < 0:
            negative_sum += num
    return negative_sum

def check(candidate):
    assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
    assert sum_negativenum([10,15,-14,13,-18,12,-20])==-52
    assert sum_negativenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==-894

check(sum_negativenum)