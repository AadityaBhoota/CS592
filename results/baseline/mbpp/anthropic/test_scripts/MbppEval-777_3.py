def find_sum(arr, n):
    """
    Finds the sum of non-repeated elements in a given list.

    Args:
        arr (list): The input list of numbers.
        n (int): The length of the input list.

    Returns:
        int: The sum of non-repeated elements in the list.
    """
    # Create a set to store unique elements
    unique_set = set()

    # Iterate through the list and add unique elements to the set
    for num in arr:
        unique_set.add(num)

    # Calculate the sum of unique elements
    return sum(unique_set)

def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)