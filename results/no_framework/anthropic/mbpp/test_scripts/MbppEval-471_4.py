def find_remainder(arr, n):
    """
    Write a python function to find the product of the array multiplication modulo n.

    Examples:
    find_remainder([100, 10, 5, 25, 35, 14], 6, 11) == 9
    find_remainder([1, 1, 1], 3, 1) == 0
    find_remainder([1, 2, 1], 3, 2) == 0
    """
    product = 1
    for num in arr:
        product *= num
    return product % n

def check(candidate):
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
    assert find_remainder([1,1,1],1) == 0
    assert find_remainder([1,2,1],2) == 0

check(find_remainder)