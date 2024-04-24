def find_sum(arr, n):
    """
    Finds the sum of non-repeated elements in a given list.

    Args:
        arr (list): The input list.
        n (int): The length of the list.

    Returns:
        int: The sum of non-repeated elements.
    """
    # Create a set to store unique elements
    unique_elements = set()

    # Iterate through the list and add unique elements to the set
    for num in arr:
        unique_elements.add(num)

    # Calculate the sum of unique elements
    sum_of_unique = sum(unique_elements)

    return sum_of_unique

# Example usage




def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)