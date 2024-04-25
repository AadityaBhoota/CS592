def find_tuples(test_list, K):
    """
    Find tuples which have all elements divisible by K from the given list of tuples.

    Args:
        test_list (list): List of tuples.
        K (int): The divisor.

    Returns:
        str: A string representation of the list of tuples that have all elements divisible by K.
    """
    # Use a list comprehension to filter the tuples
    filtered_tuples = [t for t in test_list if all(x % K == 0 for x in t)]

    # Convert the filtered tuples to a string representation
    result = str(filtered_tuples)

    return result

# Example usage




def check(candidate):
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
    assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == [(5, 25, 30)]
    assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == [(8, 16, 4)]

check(find_tuples)