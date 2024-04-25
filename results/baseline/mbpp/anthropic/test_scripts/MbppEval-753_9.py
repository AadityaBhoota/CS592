def min_k(test_list, K):
    """
    Write a function to find minimum k records from tuple list.
    
    Args:
    test_list (list of tuples): A list of tuples, where each tuple contains a string and an integer.
    K (int): The number of minimum records to be returned.
    
    Returns:
    list of tuples: A list of tuples containing the minimum K records from the input list.
    """
    # Sort the list of tuples based on the integer value in each tuple
    test_list.sort(key=lambda x: x[1])
    
    # Return the first K tuples from the sorted list
    return test_list[:K]

def check(candidate):
    assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
    assert min_k([('Sanjeev', 11), ('Angat', 5), ('Akash', 3), ('Nepin', 9)], 3) == [('Akash', 3), ('Angat', 5), ('Nepin', 9)]
    assert min_k([('tanmay', 14), ('Amer', 11), ('Ayesha', 9), ('SKD', 16)], 1) == [('Ayesha', 9)]

check(min_k)