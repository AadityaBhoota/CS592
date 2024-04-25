def is_ludic(n):
    """
    Helper function to check if a given number is Ludic.
    """
    if n <= 1:
        return True
    
    # Create a list of numbers from 1 to n
    numbers = list(range(1, n + 1))
    
    # Remove every nth number from the list
    i = 0
    while len(numbers) > 1:
        i = (i + numbers[i] - 1) % len(numbers)
        numbers.pop(i)
    
    return numbers[0] == n

def get_ludic(n):
    """
    Get all Ludic numbers smaller than or equal to a given integer.
    """
    ludic_numbers = []
    for i in range(1, n + 1):
        if is_ludic(i):
            ludic_numbers.append(i)
    return ludic_numbers

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)