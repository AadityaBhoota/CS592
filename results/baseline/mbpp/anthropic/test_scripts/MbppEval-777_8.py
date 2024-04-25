def find_sum(arr, n):
    """
    Find the sum of non-repeated elements in a given list.

    Args:
    arr (list): The input list.
    n (int): The length of the list.

    Returns:
    int: The sum of non-repeated elements in the list.
    """
    # Create a set to store unique elements
    unique_set = set()
    # Initialize the sum to 0
    total_sum = 0

    # Iterate through the list
    for num in arr:
        # If the number is not in the set, add it to the set and update the sum
        if num not in unique_set:
            unique_set.add(num)
            total_sum += num

    return total_sum

def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)