def find_remainder(arr, n):
    """
    Write a Python function to find the product of the array multiplication modulo n.

    Args:
        arr (list): The input array.
        n (int): The number to take the modulo.

    Returns:
        int: The product of the array multiplication modulo n.
    """
    product = 1
    for num in arr:
        product = (product * num) % n
    return product

def check(candidate):
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
    assert find_remainder([1,1,1],1) == 0
    assert find_remainder([1,2,1],2) == 0

check(find_remainder)