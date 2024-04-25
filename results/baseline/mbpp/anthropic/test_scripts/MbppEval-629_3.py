def Split(numbers):
    """
    Finds the even numbers from a list of numbers.
    
    Args:
    numbers (list): A list of numbers.
    
    Returns:
    list: A list of even numbers from the input list.
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

def check(candidate):
    assert Split([1,2,3,4,5]) == [2,4]
    assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]
    assert Split ([8,12,15,19]) == [8,12]

check(Split)