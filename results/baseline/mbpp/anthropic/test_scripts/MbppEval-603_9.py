def get_ludic(n):
    """
    Write a function to get all Ludic numbers smaller than or equal to a given integer.

    Examples:
    get_ludic(10) == [1, 2, 3, 5, 7]
    get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]
    """
    # Initialize the list of Ludic numbers with 1
    ludic_numbers = [1]

    # Iterate from 2 to the given integer n
    for i in range(2, n + 1):
        # Check if the current number is Ludic
        is_ludic = True
        for divisor in ludic_numbers:
            if i % divisor == 0:
                is_ludic = False
                break

        # If the current number is Ludic, add it to the list
        if is_ludic:
            ludic_numbers.append(i)

    # Return the list of Ludic numbers
    return ludic_numbers

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)