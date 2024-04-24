def Split(list):
    """
    Write a python function to find even numbers from a list of numbers.

    Examples:
    Split([1,2,3,4,5]) == [2,4]
    Split([4,5,6,7,8,0,1]) == [4,6,8,0]
    Split ([8,12,15,19]) == [8,12]
    """
    even_numbers = [num for num in list if num % 2 == 0]
    return even_numbers

def check(candidate):
    assert Split([1,2,3,4,5]) == [2,4]
    assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]
    assert Split ([8,12,15,19]) == [8,12]

check(Split)