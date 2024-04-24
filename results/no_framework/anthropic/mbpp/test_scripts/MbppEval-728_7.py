def sum_list(lst1, lst2):
    """
    Adds the corresponding elements of two lists and returns a new list.

    Args:
        lst1 (list): The first list of numbers.
        lst2 (list): The second list of numbers.

    Returns:
        list: A new list containing the sum of the corresponding elements in lst1 and lst2.
    """
    if len(lst1) != len(lst2):
        raise ValueError("Both lists must have the same length.")
    
    return [a + b for a, b in zip(lst1, lst2)]

def check(candidate):
    assert sum_list([10,20,30],[15,25,35])==[25,45,65]
    assert sum_list([1,2,3],[5,6,7])==[6,8,10]
    assert sum_list([15,20,30],[15,45,75])==[30,65,105]

check(sum_list)