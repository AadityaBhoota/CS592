def max_Product(arr): 
    '''
    Write a python function to find a pair with highest product from a given array of integers.

    Examples:
    max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    max_Product([1,2,3]) == (2,3)
    '''
def max_product(arr):
    """
    Write a Python function to find a pair with the highest product from a given array of integers.

    Examples:
    max_product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
    max_product([0, -1, -2, -4, 5, 0, -6]) == (-4, -6)
    max_product([1, 2, 3]) == (2, 3)
    """
    if len(arr) < 2:
        return None

    max_pair = (arr[0], arr[1])
    max_product = max_pair[0] * max_pair[1]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            current_product = arr[i] * arr[j]
            if current_product > max_product:
                max_pair = (arr[i], arr[j])
                max_product = current_product

    return max_pair

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)