def find_sum(arr, n):
    """
    Write a python function to find the sum of non-repeated elements in a given list.

    Args:
        arr (list): The list of integers.
        n (int): The length of the list.

    Returns:
        int: The sum of non-repeated elements in the list.
    """
    # Create a dictionary to store the count of each element
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Calculate the sum of non-repeated elements
    total_sum = 0
    for num, freq in count.items():
        if freq == 1:
            total_sum += num

    return total_sum

def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)