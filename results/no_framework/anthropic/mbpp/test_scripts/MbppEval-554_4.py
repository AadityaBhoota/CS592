def Split(list_of_integers):
    """
    Filters a list of integers and returns only the odd ones.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        list: A list containing only the odd integers from the input list.
    """
    return [num for num in list_of_integers if num % 2 != 0]

def check(candidate):
    assert Split([1,2,3,4,5,6]) == [1,3,5]
    assert Split([10,11,12,13]) == [11,13]
    assert Split([7,8,9,1]) == [7,9,1]

check(Split)